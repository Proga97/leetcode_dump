class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = 0 
        map = collections.defaultdict(int)
        l = 0
        maxf = 0 
        for r in range(len(s)):
            map[s[r]] = map[s[r]] + 1
            maxf = max(maxf, map[s[r]])
            while (r-l+1) - maxf > k :
                map[s[l]] -= 1
                l += 1
            size = max(r-l+1, size)
        # print(map)
        return size

        
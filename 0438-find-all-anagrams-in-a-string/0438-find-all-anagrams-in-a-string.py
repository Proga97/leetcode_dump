class Solution:
    def findAnagrams(self, s2: str, p: str) -> List[int]:
        p_map = Counter(p)
        l = 0
        freq = defaultdict(int)
        res = []
        for r in range(len(s2)):
            freq[s2[r]] += 1
            while l <= r and (s2[r] not in p_map or freq[s2[r]] > p_map[s2[r]]): 
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0: del freq[s2[l]]
                l += 1
            # print(freq, p_map, l , r)
            if freq == p_map: res.append(l)

        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
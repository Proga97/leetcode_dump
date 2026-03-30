class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        max_odd = 0
        odd = False
        for n in count.values():
            if n % 2 == 0: res += n
            else: 
                odd = True
                res += n - 1
        return res + 1 if odd else res
         
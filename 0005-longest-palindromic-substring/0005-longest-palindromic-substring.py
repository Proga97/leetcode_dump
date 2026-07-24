class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resL = "", 0

        for i in range(len(s)):
            # even length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resL:
                    res = s[l:r+1]
                    resL = r - l + 1
                l -= 1
                r += 1
            
            # odd length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resL:
                    res = s[l:r+1]
                    resL = r - l + 1
                l -= 1
                r += 1
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
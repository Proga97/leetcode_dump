class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr = {}
        length = 0
        for r in range(len(s)):
            if s[r] in curr and curr[s[r]] >= l:
                l = curr[s[r]] + 1
            
            curr[s[r]] = r
            
            if r - l + 1 > length:
                length = r - l + 1
        return length



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
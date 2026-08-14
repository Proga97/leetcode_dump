class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
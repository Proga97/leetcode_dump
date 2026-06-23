class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        set_char = set(s)

        for i in range(len(s)):
            c = s[i]
            if c.lower() in set_char and c.upper() in set_char:
                continue

            sub1 = self.longestNiceSubstring(s[:i])
            sub2 = self.longestNiceSubstring(s[i+1:])

            return sub1 if len(sub1) >= len(sub2) else sub2

        return s
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
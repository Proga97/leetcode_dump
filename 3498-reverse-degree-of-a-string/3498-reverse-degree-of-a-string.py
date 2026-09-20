class Solution:
    def get_index(self, c):
        return abs(ord(c) - ord("z") -1)

    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.get_index(s[i]) * (i + 1)
        
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
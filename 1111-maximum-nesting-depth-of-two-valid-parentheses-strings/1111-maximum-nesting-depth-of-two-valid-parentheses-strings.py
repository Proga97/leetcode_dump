class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        d = 0
        for c in seq:
            if c == "(":
                d += 1
                ans.append(d % 2)
            if c == ")":
                ans.append(d % 2)
                d -= 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
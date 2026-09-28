class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = 0
        for c in s:
            if stack and c == ")":
                stack -= 1
            if c == "(":
                stack += 1
                res = max(res, stack)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
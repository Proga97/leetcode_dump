class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
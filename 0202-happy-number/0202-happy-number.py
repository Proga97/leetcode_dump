class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))

        return n == 1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
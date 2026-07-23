class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1

        n1 = 0
        n2 = 1
        n3 = 1

        for i in range(3, n + 1):
            n1, n2, n3 = n2, n3, n1 + n2 + n3

        return n3
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
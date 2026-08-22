class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        prod = 1
        temp = n
        while n > 0:
            x = n % 10
            n //= 10
            total += x
            prod *= x
        return temp % (prod + total) == 0

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000: return 0
        # count = 0
        # while n > 0:
        #     n //= 10
        #     count += 1
        # return count - 1
        return n - 999
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
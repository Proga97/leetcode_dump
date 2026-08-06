class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            res = 1 
            temp = i
            while temp > 0:
                res = res * (temp % 10)
                temp = temp // 10
            if res % t == 0:
                return i
        return n

                             
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
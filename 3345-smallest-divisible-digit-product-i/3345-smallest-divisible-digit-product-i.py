class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            res = 1 
            temp = i
            while i > 0:
                res = res * (i % 10)
                i = i // 10
                # print(res, i)
            # print(res, temp, "y")
            if res % t == 0:
                return temp
        return n

                             
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        sum_n = 0
        res = ""
        for i in n:
            if i != "0":
                sum_n += int(i)
                res += i

        return sum_n * int(res) if res else sum_n
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
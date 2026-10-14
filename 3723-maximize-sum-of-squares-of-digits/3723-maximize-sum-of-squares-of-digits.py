class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum: return ""
        
        no_of_nines = sum // 9
        left = sum % 9

        res = "9" * no_of_nines

        if left > 0:
            res += str(left)
        
        res += "0" * (num - len(res))

        return res




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
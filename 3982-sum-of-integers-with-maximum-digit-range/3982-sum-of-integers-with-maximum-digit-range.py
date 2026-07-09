class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        res = 0
        max_diff = 0
        for n in nums:
            digits_list = [int(digit) for digit in str(n)]
            range_number = max(digits_list) - min(digits_list)
            if range_number > max_diff:
                max_diff = range_number
                res = n
            elif range_number == max_diff:
                res+= n
        return res







# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
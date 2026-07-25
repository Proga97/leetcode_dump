class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_n = min(nums)
        max_n = max(nums)
        for i in range(min_n, 0, -1):
            if min_n % i == 0 and max_n % i == 0:
                return i
        return 1


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
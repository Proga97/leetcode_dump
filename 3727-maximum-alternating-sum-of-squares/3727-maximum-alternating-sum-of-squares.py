class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(nums, key = lambda x: abs(x))
        r = len(nums) - 1
        l = 0
        res = 0

        while l < r: 
            res +=( nums[r]**2 - nums[l]**2)
            l += 1
            r -= 1

        if len(nums) % 2 != 0:
            res += nums[r]**2
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
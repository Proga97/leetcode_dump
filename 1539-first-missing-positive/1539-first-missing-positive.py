class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains_1 = False
        for i in range(n): 
            if nums[i] == 1: contains_1 = True
            if nums[i] <= 0 or nums[i] > n: nums[i] = 1 

        if not contains_1: return 1
        
        nums = set(nums)
        n = max(nums)
        for i in range(2, n):
            if i not in nums:
                return i

        return n + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while (low < len(nums) - 1 and nums[low] <= nums[low + 1]):
            low += 1

        if low == len(nums) - 1:  
            return 0

        while (high > 0 and nums[high] >= nums[high - 1]):
            high -= 1

        subarray_max = max(nums[low: high+1])
        subarray_min = min(nums[low: high+1])
       
        while (low > 0 and nums[low-1] > subarray_min):
            low -= 1
        
        while (high < len(nums)-1 and nums[high+1] < subarray_max):
            high += 1

        return high - low + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
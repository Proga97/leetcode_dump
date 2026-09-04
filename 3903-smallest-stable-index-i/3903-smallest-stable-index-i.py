class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        start_max = nums[0]
        suffix_min = [-1] * n
        start_min = nums[-1]

        for i in range(n-1, -1, -1):
            start_min = min(start_min, nums[i])
            suffix_min[i] = start_min
        for i in range(n):
            start_max = max(start_max, nums[i])
            # print(start_max, suffix_min[i],nums[i])
            if start_max - suffix_min[i] <= k: return i
        
        return -1




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
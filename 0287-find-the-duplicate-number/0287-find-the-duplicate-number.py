class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[j] == nums[i]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else: i += 1 
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
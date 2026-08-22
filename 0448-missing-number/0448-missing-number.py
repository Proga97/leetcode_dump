class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)

        for i in range(len(nums)):
            if i not in nums: return i
        
        return i + 1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
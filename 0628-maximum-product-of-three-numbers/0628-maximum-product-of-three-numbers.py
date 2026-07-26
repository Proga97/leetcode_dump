class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1 = 1
        if nums [0] * nums[1] * nums[-1] >= nums[-1] * nums[-2] * nums[-3]:
            return nums [0] * nums[1] * nums[-1]
        else: return nums[-1] * nums[-2] * nums[-3]


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
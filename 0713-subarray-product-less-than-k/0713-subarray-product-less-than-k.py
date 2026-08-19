class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0

        res = 0
        l = 0
        mul = 1

        for r in range(len(nums)):
            mul *= nums[r]

            while mul >= k:
                mul //= nums[l]
                l += 1
            
            res += r - l + 1
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
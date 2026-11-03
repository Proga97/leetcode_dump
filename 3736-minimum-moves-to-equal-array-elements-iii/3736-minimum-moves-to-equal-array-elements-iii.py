class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_v = max(nums)
        res = 0

        for n in nums:
            res += max_v - n
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
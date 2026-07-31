class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxL = preSum = 0
        preSumMap = {}
        for r in range(len(nums)):
            preSum += nums[r]
            
            if preSum == k:
                maxL = r + 1

            if preSum - k in preSumMap:
                maxL = max(maxL, r - preSumMap[preSum - k])
            
            if preSum not in preSumMap:
                preSumMap[preSum] = r

        return maxL

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
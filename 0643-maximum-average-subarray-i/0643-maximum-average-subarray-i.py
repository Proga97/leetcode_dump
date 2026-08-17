class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        total = 0
        for i in range(k):
            total += nums[i]
        res = max(res, total/k)

        for i in range(k, len(nums)):
            total -= nums[i-k]
            total += nums[i]
            res = max(res, total/k)
        
        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
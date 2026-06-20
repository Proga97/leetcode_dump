class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 1
        nums.sort()
        tot = 0
        l = 0
        for r in range(len(nums)):
            tot += nums[r]

            while (r - l + 1) * nums[r] > tot + k:                
                tot -= nums[l]
                l += 1
            res = max(res,r-l +1)

        return res




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
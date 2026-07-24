class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        dp = {}
        dp[0] = nums[0]
        dp[1] = nums[1]
        n = len(nums)

        for i in range(2, n):
            
            #rob alternate
            n1 = nums[i] + dp[i-2]
            # print(i, n1)
            if i > 2:
                n1 = max(n1, nums[i] + dp[i-3])
            # print(i, n1)
            dp[i] = n1
        
        return max(dp[n-1], dp[n-2])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
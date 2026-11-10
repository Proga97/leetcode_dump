class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = {}
        dp[0] = 0

        for i in range(1, n + 1):
            
            # taking one step
            step_cost = dp[i - 1] + costs[i - 1] + 1

            # 2 steps
            if i - 2 >= 0:
                step_cost = min(step_cost, dp[i - 2] + costs[i - 1] + 4)
            
            # 3 steps
            if i - 3 >= 0:
                step_cost = min(step_cost, dp[i - 3] + costs[i - 1] + 9)

            dp[i] = step_cost
        
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
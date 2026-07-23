class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 0
        n = len(cost)
        for i in range(2, n+1):
            n1 = dp[i - 1] + cost[i - 1]
            n2 = dp[i - 2] + cost[i - 2]

            dp[i] = min(n1, n2)
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
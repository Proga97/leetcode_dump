class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def dfs(i):
            if i >= len(stoneValue):
               return 0
            if i in dp:
                return dp[i]
            
            dp[i] = stoneValue[i] - dfs(i + 1)
            if i + 1 < len(stoneValue):
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dfs(i + 2))
            if i + 2 < len(stoneValue):
                dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dfs(i + 3))
            return dp[i]
        
        diff = dfs(0)
        if diff > 0: return "Alice"
        elif diff < 0: return "Bob"
        else: return "Tie"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
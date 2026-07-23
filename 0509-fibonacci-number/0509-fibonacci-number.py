class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1

        def dfs(val):
            if val in dp:
                return dp[val]
            
            next_num = dfs(val - 1) + dfs(val - 2)

            dp[val] = next_num

            return dp[val]
        
        return dfs(n)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = {}
        dp[0] = 0

        for i in range(1, n + 1):
                        
            n1 = dp[i - 1] + costs[i - 1] + 1 # 1 step
            
            if i - 2 >= 0:
                n1 = min(n1, dp[i - 2] + costs[i - 1] + 4) # 2 steps
            
            if i - 3 >= 0:
                n1 = min(n1, dp[i - 3] + costs[i - 1] + 9) # 3 steps
            
            dp[i] = n1
        
        return n1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
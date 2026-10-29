class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                for val in dp[i][j]:
                    if i + 1 < m:
                        dp[i + 1][j].add(val ^ grid[i + 1][j])

                    if j + 1 < n:
                        dp[i][j + 1].add(val ^ grid[i][j + 1])
                        
        return min(dp[m - 1][n - 1])
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
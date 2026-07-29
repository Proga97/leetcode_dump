class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}

        def dfs(x, y):
            if x == len(grid) - 1 and y == len(grid[0]) -1:
                return grid[x][y]
            if x >= len(grid) or y >= len(grid[0]):
                return float("inf")
            if (x, y) in dp:
                return dp[(x,y)]
            # print(x,y)
            dist = grid[x][y] + min(dfs(x + 1, y), dfs(x, y + 1))
            dp[(x, y)] = dist 

            return dp[(x, y)]
        
        return dfs(0,0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
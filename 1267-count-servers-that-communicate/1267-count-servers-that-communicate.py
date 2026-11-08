class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        row_count = [-1] * m
        col_count = [-1] * n
        locations = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
                    locations.append((i, j))
        
        for i, j in locations:
            if row_count[i] or col_count[j]:
                res += 1
        
        return res
        
                                




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
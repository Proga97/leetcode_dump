class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        path_len = n + m - 1

        if path_len % 2 == 1:
            return False
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(": return False

        dp = {}
        di = [(0,1), (1,0)]

        def dfs(x, y, open_count):
            open_count += 1 if grid[x][y] == "(" else -1
            if open_count < 0: return False

            if (x,y,open_count) in dp: return dp[(x,y,open_count)]

            if x == m - 1 and y == n-1: return open_count == 0

            dp[(x,y,open_count)] = False
            # print(x, y , open_count, grid[x][y])
            for dx, dy in di:
                new_x = x + dx
                new_y = y + dy
                if new_x < m and new_y < n:
                    dp[(x,y,open_count)] =  dp[(x,y,open_count)] or dfs(new_x, new_y, open_count)    

            return dp[(x,y,open_count)]
        
        # print(dp)
        return dfs(0,0,0)
                   






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        dr = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(x,y):
            stack = [(x,y)]
            val = grid[x][y]
            grid[x][y] = -1
            
            while stack:
                r, c = stack.pop()
                for dx, dy in dr:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                        val += grid[nr][nc]
                        stack.append((nr,nc))
                        grid[nr][nc] = -1
            
            return val % k == 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and dfs(i,j):
                    res += 1
        
        return res





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
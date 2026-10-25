class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            stack = [(x,y)]
            grid[x][y] = -1
            is_closed = True
            if (y == 0 or y == cols - 1 or x == 0 or x == rows - 1):
                is_closed = False
            while stack:
                x, y = stack.pop()    

                directions = [[-1,0],[0,-1],[1,0],[0,1]]
                for dr, dc in directions:
                    newC = y + dc
                    newR = x + dr
                    if newC >= 0 and newC < cols and newR >= 0 and newR < rows and grid[newR][newC] == 0:
                        grid[newR][newC] = -1
                        if (newC == 0 or newC == cols - 1 or newR == 0 or newR == rows - 1):
                            # print("false",newR,newC)
                            is_closed = False
                        stack.append((newR,newC))
                        # print(newR,newC)
                        
        
            return is_closed
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if  grid[i][j] == 0 and dfs(i,j):
                    # print("meow",i,j,count)
                    count += 1
        
        return count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
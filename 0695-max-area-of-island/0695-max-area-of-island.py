class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0
        areas = {}

        def bfs(i,j):
            qu = collections.deque()
            qu.append((i,j))
            grid[i][j] = 0
            a = 0
            while qu:
                i, j = qu.popleft()
                a += 1 
                print("checking",i,j,a)
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr, dc in directions:
                    newR = i + dr
                    newC = j + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        qu.append((newR,newC))
                        grid[newR][newC] = 0
                        print("part row",newR,newC)
            return a
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                    print("new",i,j)
                    area = bfs(i,j)
                    areas[count] = area
        
        print(areas)
        return max(areas.values()) if len(areas) > 0 else 0


            

        
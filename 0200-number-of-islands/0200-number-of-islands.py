class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         print(grid[i][j],end=" ")
        #     print()

        seen = set()
        count = 0
        rows, cols = len(grid), len(grid[0]) 
        def bfs(i,j):
            qu = collections.deque()
            qu.append((i,j))

            while qu:
                i, j = qu.popleft()
                seen.add((i,j))
                # print("checking",i,j)
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dr, dc in directions:
                    newR = i + dr
                    newC = j + dc
                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == "1" and (newR,newC) not in seen:
                        qu.append((newR,newC))
                        # print("part row",newR,newC)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    bfs(i,j)
                    # print("new",i,j)
                    count += 1

        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == "1":
        #             if  (i > 0 and grid[i-1][j] == "1") or ( j > 0 and grid[i][j-1] == "1"):
        #                 print("part",i,j)
        #                 continue
        #             else:    
        #                 count += 1
        #                 print("new",i,j)
                        
        # print(count)  
        return count
    

        
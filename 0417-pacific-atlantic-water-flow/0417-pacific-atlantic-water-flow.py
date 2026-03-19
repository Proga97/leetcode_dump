class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        pa = set()
        at = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i,j,flows):
            flows.add((i,j))
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in directions:
                newR = i + dr
                newC = j + dc
                if 0 <= newR < rows and  0 <= newC < cols and  heights[newR][newC] >= heights[i][j] and (newR,newC) not in flows:
                    dfs(newR,newC,flows)
                    
        for c in range(cols):
            dfs(0,c,pa)
            dfs(rows-1,c,at)
        
        for r in range(rows):
            dfs(r,0,pa)
            dfs(r,cols-1,at)
        
        # print(pa)
        # print(at)

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pa and (i,j) in at:
                    res.append([i,j])
        # print(res)
        return res

        
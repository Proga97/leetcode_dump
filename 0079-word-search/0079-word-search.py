class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if 0 > r  or  rows <= r or 0 > c or c >= cols or (r,c) in path or board[r][c] != word[i]:
                return False

            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            path.add((r,c))
            res = False
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                res = res or dfs(newR,newC,i+1) 
            path.remove((r,c))        
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        
        return False
                    




        
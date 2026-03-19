class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         print(board[i][j],end=" ")
        #     print()

        # valid = set()
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            # valid.add((i,j))
            board[i][j] = "C"
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            for dr, dc in directions:
                newR = i + dr
                newC = j + dc
                if 0 <= newR < rows and 0 <= newC < cols and board[newR][newC] == "O":
                    #  and (newR,newC) not in valid:
                    dfs(newR,newC)

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][cols-1] == "O":
                dfs(i,cols-1)
        
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0,j)
            if board[rows-1][j] == "O":
                dfs(rows-1,j)
        
        # print(valid)
        for i in range(len(board)):
            for j in range(len(board[i])):
                # if board[i][j] == "O" and (i,j) not in valid:
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "C":
                    board[i][j] = "O"
        

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # seen = set()
        def dfs(i, j, index):
            if index >= len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                # print("rej",i, j, index)
                return False
            # print(i, j, word[index])
            # seen.add((i, j))
            temp = board[i][j]
            board[i][j] = "#"
            
            up = dfs(i - 1, j, index + 1)
            down = dfs(i + 1, j, index + 1)
            right = dfs(i , j + 1, index + 1)
            left = dfs(i , j - 1, index + 1)
            if (up or down or right or left): 
                return True

            board[i][j] = temp
            # seen.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
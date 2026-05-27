class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns, rows, grid = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    num = board[r][c]
                    if num in rows[r] or num in columns[c] or num in grid[r//3,c//3]:
                        return False
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    grid[r//3,c//3].add(board[r][c]) 
        # print(rows)
        # print(columns)
        # print(grid)
        return True


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
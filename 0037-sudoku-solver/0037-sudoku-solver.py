class Solution:
    def init_sudoku(self, board):
        self.row_dict = defaultdict(set)
        self.col_dict = defaultdict(set)
        self.grid_dict = defaultdict(set)
        rows, cols = len(board), len(board[0])
        self.empty_cells = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    self.row_dict[r].add(board[r][c])  
                    self.col_dict[c].add(board[r][c])
                    self.grid_dict[(r//3, c//3)].add(board[r][c])
                else:
                    self.empty_cells.append((r, c))
                
    def isValid(self, num, row, col):
        if num not in self.row_dict[row] and num not in self.col_dict[col] and num not in self.grid_dict[(row//3, col//3)]:
            return True
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.init_sudoku(board)
        self.genSudoku(board, 0)

    
    def genSudoku(self, board, index):
        if index >= len(self.empty_cells):
            return True
        
        r, c = self.empty_cells[index]

        for num in range(1, 10):
            num = str(num)
            if self.isValid(num, r, c):
                self.row_dict[r].add(num)
                self.col_dict[c].add(num)
                self.grid_dict[r//3, c//3].add(num)
                board[r][c] = num

                if self.genSudoku(board, index + 1):
                    return True
                
                self.row_dict[r].remove(num)
                self.col_dict[c].remove(num)
                self.grid_dict[r//3, c//3].remove(num)
                board[r][c] = "."

        return False
                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
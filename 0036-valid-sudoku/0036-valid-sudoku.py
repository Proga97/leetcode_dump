import collections 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = collections.defaultdict(set)
        rows =  collections.defaultdict(set)
        cols =  collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
               if board[row][col] != ".":
                    num = board[row][col]
                    if num in rows[row] or num in cols[col] or num in box[row//3,col//3]:
                        # print("in",num,row,rows)
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    box[row//3,col//3].add(num)
        return True
        # print(rows,cols,box) 
                    



        
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        width = 1
        moved_east = False
        while len(res) < rows * cols:
            if not moved_east:
                for _ in range(width):                    
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                    cStart += 1
                for _ in range(width):                    
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                    rStart += 1
            else:
                for _ in range(width):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                    cStart -= 1
                for _ in range(width):                    
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                    rStart -= 1
            width += 1
            moved_east = not moved_east
        return res





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
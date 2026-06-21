class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) - 1
        c = 0
        while c < len(matrix[0]) and r >= 0:
            
            if matrix[r][c] > target:
                # print("row",matrix[r][c])
                r -= 1
                # print("row2",matrix[r][c])
            elif matrix[r][c] < target: 
                # print("column",matrix[r][c])
                c += 1
                # print("column2",matrix[r][c])
            # elif r < len(matrix) - 1 and matrix[r][c] <= target and matrix[r+1][c] <= target:
            #     print("row",matrix[r][c])
            #     r += 1
            else:
                # print("break",matrix[r][c])
                # break
                return True
        return False
            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
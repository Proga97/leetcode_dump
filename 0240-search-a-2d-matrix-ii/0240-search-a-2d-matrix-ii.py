class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) - 1
        c = 0
        while c < len(matrix[0]) and r >= 0:
            
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target: 
                c += 1
            else:
                return True
                
        return False
            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        numCols = ceil(n / (2 * numRows - 2)) * (numRows - 1)
        matrix = [["" for _ in range(numCols)] for _ in range(numRows)]
        row = 0
        col = 0
        i = 0 
        # print(numCols)
        while i < n:
            if row == 0:
                while i < n and row < numRows:
                    matrix[row][col] = s[i]
                    row += 1
                    i = i + 1
                row -= 2
                col += 1
                if row < 0:
                    row = numRows - 1
            else:
                matrix[row][col] = s[i]
                i += 1
                row -= 1
                col += 1
        res = ""
        for row in matrix:
            # print(row)
            res += "".join(row)
        return res


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
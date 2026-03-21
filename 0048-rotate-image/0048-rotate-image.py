class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range (r - l):
                top, bot = l, r 

                topLeft = matrix[top][l+i]

                # topRight = matrix[top+i][r]

                # botLeft = matrix[bot-i][l]

                # botRight = matrix[bot][r-i]

                # topLeft = botLeft
                matrix[top][l+i] = matrix[bot-i][l]
                # print("topLeft = botLeft",)

                # botLeft = botRight
                matrix[bot-i][l] = matrix[bot][r-i]

                # botRight = topRight 
                matrix[bot][r-i] = matrix[top+i][r]

                # topRight =  topLeft
                matrix[top+i][r] = topLeft

            l += 1
            r -= 1










        
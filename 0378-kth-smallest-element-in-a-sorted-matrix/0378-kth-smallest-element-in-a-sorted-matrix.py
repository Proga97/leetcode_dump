class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        index = 0
        heap = []
        n = len(matrix)
        for r in range(n):
            heappush(heap, (matrix[r][0], r, 0))
        
        while k > 1:
            number, row, col = heappop(heap)

            if col + 1 < n:
                heappush(heap, (matrix[row][col+1], row, col + 1))
            
            k -= 1

        element, r , c = heappop(heap)
        return element

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
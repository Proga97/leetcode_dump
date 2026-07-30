class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [(0,0,0)] #(maxDiff to get here, r, c)
        visited = set()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        while minHeap:
            diff, r, c = heappop(minHeap)

            if r == ROWS - 1 and c == COLS - 1:
                return diff

            if (r,c) in visited:
                continue
            
            visited.add((r,c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or (newR, newC) in visited:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heappush(minHeap, (newDiff, newR, newC))

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
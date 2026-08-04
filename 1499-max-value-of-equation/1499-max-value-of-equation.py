class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        qu = deque()
        max_val = float("-inf")
        # 1 <= i < j <= points.length
        # yi + yj + |xi - xj| =  xi + yi + yj - xj
        for x, y in points:
            while qu and x - qu[0][0] > k:
                qu.popleft()
            if qu:    
                val = x + y + qu[0][1] - qu[0][0] 
                max_val = max(val, max_val)
            while qu and qu[-1][1] - qu[-1][0] <= y - x:
                qu.pop()

            qu.append([x,y])

        return max_val  
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = defaultdict(list)
        for x, y in points:
            dist = math.sqrt(x**2 + y **2)
            dist_map[dist].append([x,y])
        
        heap = []
        for dist, cord in dist_map.items():
            for c in cord:
                heapq.heappush(heap, (-dist, c))
                if len(heap) > k:
                    heapq.heappop(heap)

        res = []
        for dist, cord in heap:
            res.append(cord)
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
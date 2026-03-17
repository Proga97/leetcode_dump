class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]  
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            diff = -abs(x1-x2)
            heapq.heappush(stones,diff)
        return abs(stones[0])

        
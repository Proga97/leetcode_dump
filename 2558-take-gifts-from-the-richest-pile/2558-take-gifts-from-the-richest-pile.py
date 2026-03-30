class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)        
        # print(max_heap)

        for _ in range(k):
            x = int(math.sqrt(abs(heapq.heappop(max_heap))))
            heapq.heappush(max_heap, -x)
        # print(max_heap)
        return -sum(max_heap)
        
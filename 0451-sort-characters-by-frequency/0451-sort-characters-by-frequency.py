import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        map_c = defaultdict(int)
        for n in s:
            map_c[n] -= 1

        heap = [(f, c) for  c,f in map_c.items()]
        # print(map_c,heap)
        heapq.heapify(heap)
        # print(heap)
        s = ""
        while heap:
            (f, c) = heapq.heappop(heap)
            # print(f,c)
            s += -f*c
        # print(s)
        return s
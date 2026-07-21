from heapq import *

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        freq_map = Counter(s)
        heap = [(-count, char) for char, count in freq_map.items()]
        heapify(heap)
        res = ""
        qu = deque()
        while heap:
            count, char = heappop(heap)
            count = -count - 1
            res += char
            qu.append((count, char))
            if len(qu) == k:
                count, char = qu.popleft()
                if count > 0:
                    heappush(heap, (-count, char))

        return res if len(res) == len(s) else ""

     
                    






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
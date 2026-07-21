from heapq import *
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_t = Counter(tasks)
        
        print(freq_t)
        heap = [(-count, char) for char, count in freq_t.items()]
        heapify(heap)
        res = ""
        
        while heap:
            counter = 0
            qu = []
            while counter <= n:
                if heap:
                    count, char = heappop(heap)
                    count += 1
                    res += char
                    if count < 0:
                        # print(count, char)
                        qu.append((count, char))
                elif qu:
                    res += "#"
                counter += 1
            
            for count, char in qu:
                heappush(heap, (count, char))
            # print(heap, res)                

        # print(res)
        return len(res)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
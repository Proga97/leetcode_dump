import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        res = 0
        while len(sticks) >  1:
            total = heappop(sticks)+heappop(sticks)
            res += total
            heappush(sticks,total)
        return res      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
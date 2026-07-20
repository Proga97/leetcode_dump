from collections import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heappush(heap, nums[i])

        for i in range(k, len(nums)):
            n = nums[i]
            if n > heap[0]:
                heappush(heap, n)
                heappop(heap)

        return heap[0]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
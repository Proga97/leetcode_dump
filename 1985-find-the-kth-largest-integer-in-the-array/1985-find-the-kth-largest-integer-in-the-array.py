class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        heap = []
        for n in nums:
            heappush(heap, int(n))
            if len(heap) > k:
                heappop(heap)
        return str(heappop(heap))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
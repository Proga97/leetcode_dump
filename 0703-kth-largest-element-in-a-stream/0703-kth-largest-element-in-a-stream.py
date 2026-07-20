class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
   
        for n in nums:
            heappush(self.heap, n)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            heappush(self.heap, val)
            heappop(self.heap)
        else:
            heappush(self.heap, val)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
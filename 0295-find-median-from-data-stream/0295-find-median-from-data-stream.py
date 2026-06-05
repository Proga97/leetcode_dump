import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap,-num)
        else:
            heappush(self.minHeap,num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap,-heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))
        # print(self.minHeap,self.maxHeap)
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            # print((self.arr[n//2] + self.arr[(n//2) - 1]) / 2,self.arr[n//2],self.arr[(n//2) - 1],self.arr)
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            # print(self.arr[n//2],self.arr)
            return -self.maxHeap[0]



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
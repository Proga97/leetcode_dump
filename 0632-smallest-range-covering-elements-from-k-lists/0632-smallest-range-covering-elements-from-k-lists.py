class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []
        low, high = float("inf"), float("-inf")
        for i in range(n):
            low = min(nums[i][0], low)
            high = max(nums[i][0], high)
            heappush(heap, (nums[i][0], i, 0))
        
        res = [low, high]
        while True:
            num, listI, idx = heappop(heap)

            if idx + 1 >= len(nums[listI]):
                break

            nextNum = nums[listI][idx + 1]
            heappush(heap, (nextNum, listI, idx + 1))
            low = heap[0][0]
            high = max(high, nextNum)
            # print(low, high)
            if high - low < res[1] - res[0]:
                res = [low, high]
            
        return res


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
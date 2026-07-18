# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target: return 0

        low, high = 0, 1
        while target >= reader.get(high):
            if target == reader.get(high):
                return high
            else: 
                high = high * 2
        # print(high)        
        while low <= high:
            mid = low + (high - low) // 2
            # print("meow,",low, high, mid)
            if target == reader.get(mid):
                return mid
            elif target > reader.get(mid):
                low = mid + 1
            else:
                high = mid - 1

        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
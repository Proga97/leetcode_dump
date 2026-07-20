# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
       
        max_index = self.find_max(mountainArr)
        # print(max_index)
        first_half = self.binarySearch(target, mountainArr, 0, max_index, True)
        if first_half != -1:
            return first_half

        second_half = self.binarySearch(target, mountainArr, max_index, mountainArr.length() - 1, False)
        return second_half

    def find_max(self, mountainArr: 'MountainArray'):
        low, high = 0, mountainArr.length() - 1
        while low < high:
            mid = low + (high - low)  // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                high = mid 
            else:
                low = mid + 1
        return low

    def binarySearch(self, target, mountainArr: 'MountainArray', low, high, isAsending):
        while low <= high:
            mid = low + (high - low)  // 2
            if target == mountainArr.get(mid):
                return mid
            if target > mountainArr.get(mid):
                if isAsending:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if isAsending:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
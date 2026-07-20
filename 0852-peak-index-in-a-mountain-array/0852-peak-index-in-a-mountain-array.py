class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
            low, high = 0, len(arr) - 1

            while low < high:
                mid = low + (high - low) // 2
                if arr[mid] > arr[mid+1]:
                    high = mid 
                else:
                    low = mid + 1
            # print(low)
            return low
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
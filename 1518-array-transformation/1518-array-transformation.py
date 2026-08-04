class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            changed = False
            prev = arr [:]
            for i in range(1,len(arr)-1):
                if prev[i-1] < prev[i] and prev[i] > prev[i+1]:  
                    arr[i] -= 1
                    changed = True
                if prev[i-1] > prev[i] and prev[i] < prev[i+1]:
                    arr[i] += 1
                    changed = True
            # if prev == arr:
                # return arr
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
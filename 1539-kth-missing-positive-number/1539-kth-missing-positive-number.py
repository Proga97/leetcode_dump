class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        max_n = max(arr)
        arr = set(arr)

        for i in range(1, max_n+ k+1):
            if i not in arr:
                k -= 1
                if k == 0: return i
        return i


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
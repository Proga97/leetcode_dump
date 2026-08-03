class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        res = 0
        for key, f in freq.items():
            if f == 1:
                res += key
    
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
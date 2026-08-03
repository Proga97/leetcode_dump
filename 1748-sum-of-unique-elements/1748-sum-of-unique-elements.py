class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, f in freq.items():
            buckets[f].append(key)
                
        if buckets[1]:
            return sum(buckets[1])
    
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
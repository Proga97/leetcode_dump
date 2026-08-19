class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(0, len(nums)):
            freq[nums[r]] += 1
            
            while r - l + 1 - freq[1] > k:
                freq[nums[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)

        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        freq = defaultdict(int)
        res = 0
        for r in range(len(nums)):
            num = nums[r]
            freq[num] += 1
            while freq[num] > k:
                freq[nums[l]] -= 1
                # if freq[nums[l]] == 0: del freq[nums[l]] 
                l += 1
            res = max(res, r - l + 1)
        return res
                 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
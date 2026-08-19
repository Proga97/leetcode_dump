class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        l = 0
        res = 0
        for r in range(0, len(nums)):
            if nums[r] == 0: zeros += 1
            
            while zeros > k:
                if nums[l] == 0: zeros -= 1
                l += 1
            
            res = max(r - l + 1, res)

        return res

                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
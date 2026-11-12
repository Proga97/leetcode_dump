class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ass, des, res = 1, 1, 1

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]: 
                ass += 1
                des = 1
            elif nums[i] < nums[i-1]: 
                ass = 1
                des += 1
            else:
                ass = 1
                des = 1
            res = max(res, ass, des)
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
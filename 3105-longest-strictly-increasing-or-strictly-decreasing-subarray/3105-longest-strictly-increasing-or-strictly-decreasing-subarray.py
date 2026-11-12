class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ass = [nums[0]]
        des = [nums[0]]

        res = 1

        for i in range(1,len(nums)):
            if nums[i] > ass[-1]: 
                ass.append(nums[i])
                des = [nums[i]]
            elif nums[i] < ass[-1]: 
                ass = [nums[i]]
                des.append(nums[i])
            else:
                ass = [nums[i]]
                des = [nums[i]]
            res = max(res, len(ass), len(des))
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
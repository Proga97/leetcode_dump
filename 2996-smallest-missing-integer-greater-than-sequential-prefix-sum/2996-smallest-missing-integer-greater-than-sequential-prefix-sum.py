class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res = []
        res.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i -1] + 1:
                res.append(nums[i])
            else:
                break
        
        total = sum(res)
        nums = set(nums) 
        while total in nums:
            total += 1
                
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
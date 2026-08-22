class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(0,n):
            if i + 1 not in nums:
                res.append(i+1)
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0 
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else: i += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1: res.append(nums[i])

        return res


                    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
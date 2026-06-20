class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i <= len(nums)-3:
            if nums[i+2] - nums[i] <=k:
                res.append([nums[i],nums[i+1],nums[i+2]])
                i = i + 3
            else: return []
        # print(res)
        return res
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
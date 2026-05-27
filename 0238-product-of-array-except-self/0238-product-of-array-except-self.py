class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i + 1]
        # print(suffix)
        prefix = 1
        res = []
        for i in range(0, len(nums)):
            res.append(prefix*suffix[i])
            prefix *= nums[i]
        # print(res)
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
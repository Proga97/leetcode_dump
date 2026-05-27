class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif total < 0:
                        l += 1
                    else: 
                        r -= 1
        # print(res)
        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
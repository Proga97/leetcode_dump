class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            h = len(nums) - 1
            while l < h:
                total = nums[i] + nums[l] + nums[h]
                if total == target: return total
                if abs(res) > abs(total - target): 
                    res = total - target
                if total < target: l += 1
                else: h -= 1


        return res + target



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
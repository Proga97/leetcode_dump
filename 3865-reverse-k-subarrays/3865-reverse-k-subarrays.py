class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        sets = len(nums)// k

        for i in range(k):
            l = i * sets
            r = l + sets - 1
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        return nums
            


        


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
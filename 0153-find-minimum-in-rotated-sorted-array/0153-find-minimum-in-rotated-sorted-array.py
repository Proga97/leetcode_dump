class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while right > left:
            mid = (left + right) // 2
            # print(left, right, mid)
            if nums[mid] < nums[right]:
                right = mid
            else: 
                left = mid + 1
        return nums[left]



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
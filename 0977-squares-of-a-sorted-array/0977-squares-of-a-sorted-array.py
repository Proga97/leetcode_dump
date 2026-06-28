class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        nums=[num**2 for num in nums] 
        squares=[]
        while left<=right:
            if nums[left]>nums[right]:
                squares.append(nums[left])
                left+=1
            else: 
                squares.append(nums[right])
                right-=1
        squares[:]=squares[::-1]
        return squares

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
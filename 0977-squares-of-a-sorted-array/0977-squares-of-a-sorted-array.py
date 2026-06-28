class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        squares = [0 for x in range(n)]
        highestSquareIdx = n - 1
        left, right = 0, n - 1
        
        while left <= right:
            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]
            
            if leftSquare > rightSquare:
                squares[highestSquareIdx] = leftSquare
                left += 1
            else:
                squares[highestSquareIdx] = rightSquare
                right -= 1
            
            highestSquareIdx -= 1

        return squares

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
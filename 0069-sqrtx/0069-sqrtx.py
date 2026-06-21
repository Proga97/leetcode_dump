class Solution:
    def mySqrt(self, x: int) -> int:
        high = x//2 + 1
        low = 1
        while low <= high:
            mid = low + (high - low) // 2
            sq = mid * mid
            if sq > x:
                high = mid -1
            elif sq < x:
                low = mid + 1
            else: return mid
        return high

        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
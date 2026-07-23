class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        n1 = 1
        n2 = 2

        for i in range(3, n+1):
            count =  n1 + n2 
            if i == n:
                return count
            n1 = n2
            n2 = count
        
        return n2

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
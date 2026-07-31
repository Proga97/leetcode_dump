class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        min_v = nums[0]
        stack = []
        for n in nums[1:]:
            
            min_v = min(min_v, n)

            while stack and stack[-1][0] <= n:
                stack.pop()

            if stack and stack[-1][0] > n and stack[-1][1] < n:
                return True

            stack.append([n, min_v])
        
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
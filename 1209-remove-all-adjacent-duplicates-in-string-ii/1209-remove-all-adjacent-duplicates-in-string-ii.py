class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][1] == char:
                stack[-1][0] += 1
            else:    
                stack.append([1,char])
            if stack[-1][0] == k:
                stack.pop()
            
        return "".join(c*s for c, s in stack)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
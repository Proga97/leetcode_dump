class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        stack.append(pushed[0])
        i = 1
        pop_i = 0

        while i < len(pushed) or pop_i < len(popped):
            if stack and pop_i < len(popped) and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1
            else:
                if i < len(pushed): 
                    stack.append(pushed[i])
                    i += 1
                else: return False
                
        return len(stack) == 0


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
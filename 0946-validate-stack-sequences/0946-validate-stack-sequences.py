class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_i = 0

        for n in pushed:
            stack.append(n)
            while stack and pop_i < len(popped) and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1

                
        return len(stack) == 0


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
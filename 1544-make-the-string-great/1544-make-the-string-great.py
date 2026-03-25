class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for st in s:
            if stack and st.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(st)
        return "".join(stack)
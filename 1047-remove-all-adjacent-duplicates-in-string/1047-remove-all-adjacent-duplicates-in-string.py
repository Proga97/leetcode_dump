class Solution:
    def removeDuplicates(self, s: str) -> str:
        if s is None or s.strip() == "":
            return ""
        stack = []
        for i,st in enumerate(s):
                if stack and stack[-1] == st:
                    stack.pop()
                else:
                    stack.append(st)
        return "".join(stack)
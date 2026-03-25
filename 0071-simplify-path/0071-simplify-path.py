class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        i = 0
        for n in path.split("/"):
            # print(n)
            if n == "..":
                if stack:
                    stack.pop()
            elif n and n != ".":     
                stack.append(n)
           
        return "/"+"/".join(i for i in stack)
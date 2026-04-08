class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        count = 0 
        stack = []
        for i in range(len(isConnected)):
            if i not in seen:
                count+=1
                stack.append(i)
                while stack:
                    x = stack.pop()
                    if x in seen:
                        continue
                    seen.add(x)
                    for j in range(len(isConnected)):  
                        if isConnected[x][j] == 1 and j not in seen:
                            stack.append(j)

        return count


        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = [False] * len(isConnected)
        count = 0
        stack = []

        for i in range(len(isConnected)):
            if not seen[i]:
                stack.append(i)
                count += 1  
                while stack:
                    n = stack.pop()
                    for j in range(len(isConnected[n])):
                        if isConnected[n][j] and not seen[j]:
                            stack.append(j)
                            seen[j] = True

                            
        return count





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
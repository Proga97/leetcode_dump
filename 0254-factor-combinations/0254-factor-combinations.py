class Solution:
    def getFactors(self, n: int) -> List[List[int]]:        
        res = []

        def dfs(val, divident, path):
            # print(val, divident, path)
            if path:
                res.append(path[:] + [divident])

            for i in range(val, int(divident ** 0.5) + 1):
                if divident % i == 0:
                    # path.append(i)
                    dfs(i, divident // i, path + [i])
                    # path.pop()
            
            return
        
        dfs(2, n, [])
        return res
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
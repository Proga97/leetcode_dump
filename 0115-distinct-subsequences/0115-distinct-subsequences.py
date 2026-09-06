class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = {}
        def dfs(string, i, j):
            if (i,j) in dp: return dp[(i,j)]
            # print("start",string, i, len(s), j, len(t))
            # if (i,j,string) in seen: return
            if i == m or j == n: 
                if j == n: return 1
                else: return 0
            
            res = dfs(string, i + 1, j)
            if s[i] == t[j]:
                res += dfs(string + s[i], i + 1, j + 1)
            
            dp[(i, j)] = res
            # seen.add((i,j,string))
            return dp[(i,j)]
        
        return dfs("", 0, 0)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
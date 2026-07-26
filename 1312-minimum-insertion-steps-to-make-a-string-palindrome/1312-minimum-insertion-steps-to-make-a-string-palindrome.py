class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[-1] * len(s) for _ in range(len(s))]

        def dfs(l, r):
            if l > r or l == r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = dfs(l+1, r-1)
                return dp[l][r]
            
            dp[l][r] = min(dfs(l,r-1) + 1, dfs(l+1, r) + 1)
            return dp[l][r]
        
        return dfs(0,len(s) - 1)
            



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
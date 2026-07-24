class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def dfs(l, r):
            if (l, r) in dp:
                return dp[(l,r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                dp[(l,r)] = dfs(l+1, r-1) + 2
            else:
                dp[(l,r)] = max(dfs(l+1, r), dfs(l, r-1)) 
            
            return dp[(l,r)]
        
        return dfs(0, len(s) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
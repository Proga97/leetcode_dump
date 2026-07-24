class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = {}
        # for i in range(len(s)):
        #     dp[(i,i)] = True
        #     count += 1

        def dfs(l, r):
            nonlocal count
            if (l,r) in dp:
                return dp[(l,r)]
            if l > r:
                # count += 1
                dp[(l,r)] = True
                return True
            if l == r:
                count += 1
                dp[(l,r)] = True
                return True  
            
            if s[l] == s[r]:
                if dfs(l+1, r-1):
                    dp[(l,r)] = True
                    count += 1
                else:
                    dp[(l,r)] = False
            else:
                dp[(l,r)] = False

            dfs(l+1, r)
            dfs(l, r-1)
            return dp[(l,r)]  

        dfs(0, len(s) - 1)
        return count              
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp = [1] # [""] -> ["", "a"] 
        # last = {}        
        # for i in range(len(s)):
        #     dp.append(dp[-1] * 2)
        #     if s[i] in last:
        #         dp[-1] -= dp[last[s[i]]]
        #     last[s[i]] = i

        # return (dp[-1] - 1) % MOD

        res = 0 # []
        dp = defaultdict(int)
        for c in s:
            new = res + 1 - dp[c] #["a"] -> ["a", "ab", "b"] +1 for the single cause no empty""
            res = (res + new) % MOD
            dp[c] += new

        return res % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
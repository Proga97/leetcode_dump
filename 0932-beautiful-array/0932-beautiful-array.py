class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = { 1: [1]}
        def dfs(n):
            if n not in memo:
                odd = self.beautifulArray((n + 1) // 2)
                even = self.beautifulArray(n // 2)
                memo[n] = [2 * x - 1 for x in odd] + [2 * x for x in even]
            return memo[n]
        return dfs(n)
        # ans = [1]
        # while len(ans) < n:
        #     ans = [i*2 - 1 for i in ans] + [i*2 for i in ans]
        # return [i for i in ans if i <= n]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
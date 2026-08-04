class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 2)
        # Deque stores indices j such that dp[j] values are in strictly increasing order
        q = deque()
        # Work backward from the last fruit down to fruit 1 (1-based index)
        for i in range(n, 0, -1):
            # 1. Remove indices from the right of deque if their dp values are >= current dp[i + 1]
            #    (Since dp[i + 1] is smaller and further left, it dominates them)
            while q and dp[q[-1]] >= dp[i + 1]:
                q.pop()
            
            q.append(i + 1)

            # 2. Remove indices from the left of deque that are out of range (> 2 * i + 1)
            while q and q[0] > 2 * i + 1:
                q.popleft()

            # 3. The front of deque contains the minimum dp[j] in range [i + 1, 2 * i + 1]
            #    For 2 * i >= n, dp[i] is just prices[i - 1] since dp[n + 1] = 0
            if 2 * i >= n:
                dp[i] = prices[i - 1]
            else:
                dp[i] = prices[i - 1] + dp[q[0]]

        return dp[1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
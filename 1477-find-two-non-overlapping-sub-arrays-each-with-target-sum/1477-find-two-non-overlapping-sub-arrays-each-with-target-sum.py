class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        res = n + 1
        total = 0
        lengths = []
        dp = [n] * (n + 1)
        l, r = 0, 0
        while r < len(arr):
            total += arr[r]
            while total > target:
                total -= arr[l]
                l += 1

            dp[r+1] = dp[r]

            if total == target: 
                # length = r-l+1
                # if length <= min_l:
                #     min_l_2 = min_l
                #     min_l = length
                # elif length < min_l_2: 
                #     min_l_2 = length

                # lengths.append((r-l+1, arr[l:r+1]))
                # total = 0
                # l = r + 1
                res = min(res, r - l +1 + dp[l])
                dp[r +1] = min(dp[r], r - l + 1)
            
            r += 1
        # print(lengths)
        return res if res != n + 1 else -1




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
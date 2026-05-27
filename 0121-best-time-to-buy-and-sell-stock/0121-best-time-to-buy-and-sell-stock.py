class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        low = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            price = prices[i]
            low = min(low, price)
            if price > low:
                max_profit = max(price - low, max_profit)
        return max_profit
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
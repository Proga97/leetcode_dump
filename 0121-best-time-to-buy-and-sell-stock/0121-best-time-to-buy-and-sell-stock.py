class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0
        for price in prices:
            if price < low:
                low = price
            if price - low > max_profit:
                max_profit = price - low
        return max_profit
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
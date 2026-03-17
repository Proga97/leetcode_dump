class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float('inf')
        for price in prices:
            if lowest > price:
                lowest = price
            # print(lowest,price, profit)
            profit = max(profit,price-lowest)
        return profit




                

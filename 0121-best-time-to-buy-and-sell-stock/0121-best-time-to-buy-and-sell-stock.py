class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = float("inf")
        profit = 0

        for price in prices:
            if min_val > price:
                min_val = price

            profit = max(price-min_val,profit)
        
        return profit

        
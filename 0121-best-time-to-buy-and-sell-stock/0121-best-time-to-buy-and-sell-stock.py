class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float("inf")
        profit = 0

        for price in prices:
            if min_val > price:
                min_val = price
            
            if price-min_val > profit:
                profit = price - min_val
        
        return profit
        
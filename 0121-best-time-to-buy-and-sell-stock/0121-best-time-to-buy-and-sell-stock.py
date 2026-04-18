class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        l = 0
        

        for r in range(1,len(prices)):
            if prices[r]> prices[l]:
                profit = prices[r] - prices[l]
                answer = max(answer,profit)
            else:
                l=r
        return answer
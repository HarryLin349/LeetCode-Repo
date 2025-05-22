class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max(profit, prices[i] - buy)
        return profit
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # idea: we buy at each low and sell at each high
        # maxprofit -> we only profit at each rise -> we only care when stock goes up
        # i.e. at each step if the stock went up, we buy 
        profit = 0
        prev = prices[0]
        for i in range(len(prices)):
            if prev < prices[i]:
                profit += prices[i] - prev
            prev = prices[i]
        return profit
            

# more optimal
# runtime O(n), memory O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # naively: use DP
        # idea: greedy. with unlimited buys we can just count upswings
        n = len(prices)
        if (n < 2):
            return 0
        for i in range(n):
            if i > 0:
                upswing = prices[i] - prices[i-1]
                if (upswing > 0):
                    maxProfit += upswing 
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxProfit = 0
        length = len(prices)
        while (r < length):
            if (prices[r] < prices[l]):
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return max(0, maxProfit)
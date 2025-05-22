class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #idea: dp
        # dp[i][j] = most profit from day i..n given you can buy, with j being 0 or 1 = own or not
        # can buy, sell (skip next day), or hold
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)] 
        def dp(i,j):
            if i >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            opt1, opt2, opt3 = -1, -1, -1
            # case 1: buy
            if j == 0:
                opt1 = dp(i + 1, 1) - prices[i]
            # case 2: sell
            else:
                opt2 = prices[i] + dp(i + 2, 0)
            # case 3: wait/hold
            opt3 = dp(i+1, j)
            result = max(opt1, opt2, opt3)
            memo[i][j] = result
            return result
        return dp(0,0)
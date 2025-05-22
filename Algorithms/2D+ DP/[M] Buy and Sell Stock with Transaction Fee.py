class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # idea: dp[i][j] --> max profit from i .. n given you have or don't 0/1
        # either take or don't take
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)]
        
        def dp(i,j):
            if i >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            opt1, opt2, opt3 = 0,0,0
            # buy
            if (j == 0):
                opt1 = dp(i+1, 1) - prices[i]
            else:
                # sell
                opt2 = dp(i+1, 0) + prices[i] - fee
            opt3 = dp(i+1,j)
            memo[i][j] = max(opt1,opt2,opt3)
            return memo[i][j]
        return dp(0,0)
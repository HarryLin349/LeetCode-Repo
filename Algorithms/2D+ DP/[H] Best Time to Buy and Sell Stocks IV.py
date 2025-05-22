class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # idea: dp[i][j][k] --> max profit from i .. n given you have or don't 0/1, k is remaining buys
        # either take or don't take
        n = len(prices)
        memo = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        
        def dp(i,j,k):
            if i >= n:
                return 0
            if memo[i][j][k] != -1:
                return memo[i][j][k]
            opt1, opt2, opt3 = 0,0,0
            # buy
            if (j == 0) and k > 0:
                opt1 = dp(i+1, 1, k -1) - prices[i]
            elif (j== 1):
                # sell
                opt2 = dp(i+1, 0,k) + prices[i]
            opt3 = dp(i+1,j,k)
            memo[i][j][k] = max(opt1,opt2,opt3)
            return memo[i][j][k]
        return dp(0,0,k)
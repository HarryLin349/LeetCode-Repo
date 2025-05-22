# runtime O(n), memory O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        # naively: use DP
        # dp[i][j] = max profit at i...n given j = (0/1) (own stock/don't own stock)
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)]
        def dp(i,j):
            if i >= n:
                return 0
            if (memo[i][j] != -1):
                return memo[i][j]
            # buy (if we can)
            opt1, opt2, opt3 = 0,0,0
            if (j == 0):
                opt1 = dp(i+1, 1) - prices[i]
            # sell (if we can)
            if (j == 1):
                opt2 = dp(i + 1, 0) + prices[i]
            # hold
            opt3 = dp(i+1, j)
            memo[i][j] = max(opt1,opt2,opt3)
            return memo[i][j]
        return dp(0,0)

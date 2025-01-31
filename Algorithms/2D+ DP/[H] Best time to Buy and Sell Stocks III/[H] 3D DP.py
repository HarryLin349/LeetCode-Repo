class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # naively: dp, i is index, j is own, k is remaining buys
        # technically n * 2 * 2 = n*4 = O(n) time and space
        n = len(prices)
        memo = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        def dp(i,j,k):
            if i >= n:
                return 0
            if memo[i][j][k] != -1:
                return memo[i][j][k]
            opt1, opt2, opt3 = 0,0,0
            # buy
            if (j == 0 and k > 0):
                opt1 = dp(i+1, 1, k - 1) - prices[i]
            # sell
            if (j ==1):
                opt2 = dp(i +1, 0, k) + prices[i]
            # hold
            opt3 = dp(i+1,j,k)
            memo[i][j][k] = max(opt1,opt2,opt3)
            return memo[i][j][k]
        return dp(0,0,2)
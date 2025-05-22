class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # for coin in coins:
        #   sol += dp(amount - coin)
        # avoid duplicates? only do coins >= index
        # so dp(i,j) where i is amount and j is last coin ind taken
        n = len(coins)
        memo = [[-1 for _ in range(n + 1)] for _ in range(amount + 1)]

        for i in range(n):
            memo[0][i] = 1

        def dfs(amount, idx):
            if amount == 0:
                return 1
            if amount < 0 or idx >= n:
                return 0
            if memo[amount][idx] != -1:
                return memo[amount][idx]
            sol = dfs(amount - coins[idx], idx) + dfs(amount, idx+1)
            memo[amount][idx] = sol
            return sol
        res = dfs(amount,0)
        return res

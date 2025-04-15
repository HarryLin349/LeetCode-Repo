class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INTMAX = 10**4 + 1
        # idea: DP? at each value, choose to collect a certain coin
        # dp(i) = min number of coins to reach amount i
        # recurrence:
        # for each coin option, take it and do
        # sol = 1 + dp(i - coin value)
        # base case:
        # if amount = 0, return 0
        # if amount < 0, return int max?

        memo = [-1] * (amount + 1)

        def dfs(amount):
            if (amount == 0):
                return 0
            if amount < 0:
                return INTMAX
            if memo[amount] != -1:
                return memo[amount]
            csol = INTMAX
            for coin in coins:
                csol = min(csol, 1 + dfs(amount - coin))
            
            memo[amount] = csol
            return memo[amount]
        
        result = dfs(amount)
        return result if result < INTMAX else -1
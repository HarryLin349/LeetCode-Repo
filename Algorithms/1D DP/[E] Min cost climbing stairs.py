class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # let dp[i] be the cost of climbing from the ith step 
        # idea: dp[i] = cost[i] + min(dp[i + 1] + dp[i+2])
        n = len(cost)
        dp = [0 for i in range(n + 1)]
        dp[n] = 0
        for i in reversed(range(n)):
            step1 = dp[i+1] if i+1 <= n else 0
            step2 = dp[i+2] if i+2 <= n else 0
            dp[i] = cost[i] + min(step1, step2)
        return min(dp[0], dp[1])
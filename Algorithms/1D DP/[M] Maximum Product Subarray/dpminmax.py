class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        '''
        idea
        dp, dp[i] is the max product from i to n assuming we take i 
        dp[i] is either nums[i] * dp[i+1], or nums[i] (assuming we don't take it)
        '''
        n = len(nums)
        memo = [-1 for _ in range(n)]

        def dp(i):
            if i >= n:
                return (1,1)
            if (memo[i] != -1):
                return memo[i]
            maxp, minp = dp(i+1)
            sol1, sol2 ,sol3 = nums[i], nums[i]  * maxp, nums[i] * minp
            memo[i] = (max(sol1, sol2,sol3), min(sol1,sol2,sol3))
            return memo[i]
        dp(0)
        maxproduct = nums[0]
        for i in range(n):
            maxproduct = max(maxproduct, memo[i][0])
        return maxproduct

# 13%
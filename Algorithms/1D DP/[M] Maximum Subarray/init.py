class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        '''
        ideas:
        naively, we could generate all subarray sums
        but this seems too slow
        optimizations.. prefixes? 
        dp[i] = best subarray that starts at i
        dp[i] = max of nums[i], nums[i]+dp[i+1]
        then take the max of dp[0..n]
        '''
        n = len(nums)
        memo = [-1 for _ in range(n)]

        # gives max subarray assuming you start with i to n.
        def dp(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            sol1, sol2 = 0,0
            sol1 = nums[i] # assume we end the subarray here and only take i
            sol2 = nums[i] + dp(i+1)
            memo[i] = max(sol1,sol2)
            return memo[i]
        res = nums[0]
        dp(0)
        for i in range(n):
            res = max(res, memo[i])
        print(memo)
        return res

# 5%..
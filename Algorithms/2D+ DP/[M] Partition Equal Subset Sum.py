from collections import deque
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        idea: dp, want a subset of nums == target
        dp(i,j) = from i..n, we can reach j
        want dp(0, target)
        at each,
            take: dp(i,j) = dp(i-1, j-nums[i])
            dont take: dp(i,j) = dp(i-1, j)
            dp(x,0) = true
        '''
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        memo = [[-1 for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            memo[i][0] = 1
        def dp(i,j):
            if i >= n:
                return False
            if memo[i][j] != -1:
                return memo[i][j]
            sol1, sol2 = 0,0
            # we take the current
            if (j - nums[i] >= 0):
                sol1 = dp(i+1, j-nums[i])
            # we dont take the current
            sol2 = dp(i+1, j)
            memo[i][j] = max(sol1, sol2)
            return memo[i][j]
        return dp(0,target) == 1
class Solution:
    def rob(self, nums: list[int]) -> int:
        # dp[i] is the max profit from house i..n
        # dp[i] = max of cost i + dp[i + 2]
        #           or dp[i+1]
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[n-1] = nums[n-1]
        for i in reversed(range(n)):
            adj = nums[i] + (dp[i+2] if i+2 < n else 0)
            skip = dp[i+1] if i + 1 < n else 0
            dp[i] = max(adj, skip)
        print (dp)
        return dp[0]
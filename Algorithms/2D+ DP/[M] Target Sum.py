class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # idea: dp
        # dp(i, j) represents from i..n, the sum is equal to j
        # base case: if i <= 0 and j == target, return 1
        # recursive case: 
        # take positive --> dp(i - 1, j + nums[i])
        # take negative --> dp(i - 1, j - nums[i])
        # return positive and negative
            
        n = len(nums)
        self.memo = [[-1 for _ in range(2001)] for _ in range(n)]
        return self.dp(n -1, 0, nums, target)

    def dp(self, i, csum, nums, target):
        if i < 0:
            return 1 if csum == target else 0
        if (self.memo[i][csum + 1000] != -1):
            return self.memo[i][csum + 1000]
        positives = self.dp(i -1, csum + nums[i], nums, target)
        negatives = self.dp(i -1, csum - nums[i], nums, target)
        self.memo[i][csum + 1000] = positives + negatives
        return positives + negatives


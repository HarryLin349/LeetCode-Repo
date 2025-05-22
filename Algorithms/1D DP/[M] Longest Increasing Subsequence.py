class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        '''
         idea: dp.. tuples?

         base case: i >= n, length of 0

         at each, we either take the num (+1) or dont

         when can we take? when cur num is < last taken
         dp(i,j) = best subseq at, given last taken was at j
         take:
         dp(i,j) = 1 + dp(i+i,i)
         dont take:
         dp(i,j) = dp(i+i, j)

         dp(i) represents the longest subseq that starts with i
        '''
        n = len(nums)
        memo = [1 for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i,n):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1+memo[j])
        print (memo)
        return max(memo)

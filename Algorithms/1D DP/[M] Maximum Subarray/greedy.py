class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        idea: greedily, we throw out the cur subarray if it ever goes negative
        '''
        curSum = 0
        maxSum = nums[0]
        n = len(nums)
        for i in range(n):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if (curSum < 0):
                curSum = 0

        return maxSum

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        csum, maxSum = 0, nums[0]
        for num in nums:
            csum = max(num, csum + num)
            maxSum = max(maxSum, csum)
        return maxSum
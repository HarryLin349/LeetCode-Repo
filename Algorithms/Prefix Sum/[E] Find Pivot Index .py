class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        idea: track cur sum going left
        if leftsum == total - cur, we have a match
        '''
        total = sum(nums)
        cursum = 0
        for i in range(len(nums)):
            if cursum == total - nums[i] - cursum:
                return i
            cursum += nums[i]
        return -1
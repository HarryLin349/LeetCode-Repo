class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        opt(i) ->  note that jumps past valid jumps
        are also valid
        so we only track the last valid position to see if we
        can reach it
        '''
        n = len(nums)
        lastPos = n - 1
        for i in reversed(range(n)):
            if nums[i] + i >= lastPos:
                lastPos = i
        return lastPos == 0
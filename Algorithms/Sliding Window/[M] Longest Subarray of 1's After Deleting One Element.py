class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        '''
        idea: treat this as we have 1 "skip"
        l,r is the cur subarray, l,r = 0
        res, cur
        for r in range(len(nums))
            if r is 1, cur += 1
            elif skip = 1
                skip -= 1
            else:
                while l <= r and skip < 0:
                    if nums[l] = 0:
                        skip +=  1
                    l += 1
                    cur -= 1
        '''
        res, skip = 0,1
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if skip == 1:
                    skip -= 1
                else:
                    skip -=1
                    while l <= r and skip < 0:
                        if nums[l] == 0:
                            skip += 1
                        l += 1
            res = max(res, r-l+1 - 1)
        return res
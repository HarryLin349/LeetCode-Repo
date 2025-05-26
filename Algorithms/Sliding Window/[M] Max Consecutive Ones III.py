class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        idea
        we can flip k 0's
        have pointers l,r
        at each iteration, evaluate r
            if r == 1, we have a valid string
            if r == 0 and we have remaining flips, we have a valid string
            if r == 0 and we have no remaining flips, we increase l until we get back a flip (valid)
        then we update max = r - l + 1
        and increase r
        '''
        l, r = 0,0
        remaining = k
        longest = 0
        while r < len(nums):
            if nums[r] == 0 and remaining > 0:
                remaining -= 1
            elif nums[r] == 0:
                remaining -= 1 
                while l <= r and remaining < 0:
                    if nums[l] == 0:
                        remaining += 1
                    l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest


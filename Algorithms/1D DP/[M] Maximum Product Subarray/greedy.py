class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        pmax, pmin = 1, 1

        '''
        idea: either multiply by the prevmax and prevmin
        or start a new subarray
        '''

        for i in range(len(nums)):
            tmpmax, tmpmin = pmax, pmin
            pmax = max(nums[i], nums[i]*tmpmax, nums[i]*tmpmin)
            pmin = min(nums[i],nums[i]*tmpmax, nums[i]*tmpmin)
            res = max(res, pmax)
            # print ("at ",i,nums[i], pmin, pmax)
        return res
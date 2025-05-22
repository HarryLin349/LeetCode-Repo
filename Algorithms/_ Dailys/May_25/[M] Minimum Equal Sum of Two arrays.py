class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        '''
        idea: greedily check
        if we have any zeroes q, we can scale the array from >= n + q 
        the min sum will be the max of n+q between the two
        impossible case is if q = 0 for an arr and that arr is less than the others n+q
        '''
        sum1, sum2, z1, z2 = 0,0,0,0
        for n in nums1:
            sum1 += n
            if n == 0:
                z1+=1
        for n in nums2:
            sum2 += n
            if n==0:
                z2+=1
        
        if (z1 == 0 and sum1 < sum2 + z2):
            return -1
        if (z2 == 0 and sum2 < sum1 + z1):
            return -1
        return max(sum1+z1, sum2+z2)

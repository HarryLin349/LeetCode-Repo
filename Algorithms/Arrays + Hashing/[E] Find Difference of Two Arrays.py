class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        '''
        set 1 -> all distinct ints in nums 1 which arent in num 2
        set 2 - > all distinct ints in nums 2 not in nums1
        disjoint sets? rm common elements
        naively, make a set of each
        for each elem, if its in the other, remove from both
        '''
        s1, s2 = set(nums1), set(nums2)
        answer = [[],[]]
        for n in s1:
            if n not in s2:
                answer[0].append(n)
        for n in s2:
            if n not in s1:
                answer[1].append(n)
        return answer

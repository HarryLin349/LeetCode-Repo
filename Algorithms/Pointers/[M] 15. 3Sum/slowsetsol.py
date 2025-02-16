class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # review: 2sum is O(n) where we hash each elems opp
        # and then check to see if it exists
        # we could run 2sum given each first num for O(n^2)
        # idea two: sort array, and then for each num,
        # run 2sum on target - num
        def twoSum(snum, target,i):
            answers = []
            l, r = i+1, len(snum) - 1
            while (l < r):
                csum = snum[l] + snum[r]
                if (csum < target):
                    l+= 1
                elif csum > target:
                    r -= 1
                else:
                    answers.append((snum[i], snum[l],snum[r]))
                    l += 1
            return answers
        snums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            cmatch = twoSum(snums, 0 - snums[i], i)
            if len(cmatch) > 0:
                for match in cmatch:
                    result.add(match)
        # turn set into list
        resarr = []
        for elem in result:
            resarr.append(list(elem))
        return resarr

        


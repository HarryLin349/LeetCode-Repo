class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # review: 2sum is O(n) where we hash each elems opp
        # and then check to see if it exists
        # we could run 2sum given each first num for O(n^2)
        # idea two: sort array, and then for each num,
        # run 2sum on target - num
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            # skip duplicate is 
            if i > 0 and nums[i] == nums[i -1]:
                continue
            # now run 2sum on the remaining
            j = i + 1
            k = n -1
            while (j < k):
                csum = nums[i] + nums[j] + nums[k]
                if (csum < 0):
                    j += 1
                elif (csum > 0):
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j += 1
        return res


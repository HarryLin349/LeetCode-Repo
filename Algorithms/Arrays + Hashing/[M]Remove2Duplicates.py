# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        idx = 2
        while idx < len(nums):
            prev2 = nums[idx-2]
            if nums[idx] == prev2:
                nums.pop(idx)
            else:
                idx += 1
        return idx
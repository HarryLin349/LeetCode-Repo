class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for num in nums:
            if (num != 0):
                nums[ind] = num
                ind += 1
        for i in range(ind, len(nums)):
            nums[i] = 0
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                counter -= 1
                nums.pop(i)
            else:
                i += 1
        return counter
    

'''
Optimized Solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

'''
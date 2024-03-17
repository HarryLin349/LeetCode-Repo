class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea: traverse array and remove zeroes
        # then add back at the end 
        
        curInd = 0
        numZeroes = 0
        while (curInd < len(nums)):
            if (nums[curInd] == 0):
                nums.pop(curInd)
                numZeroes += 1
            else:
                curInd += 1
        for i in range(numZeroes):
            nums.append(0)
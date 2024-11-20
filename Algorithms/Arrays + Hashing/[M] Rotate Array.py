class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idea: k steps to the right
        # newIndex = index + k % len
        # for each index, set it to newIndex
        # issue is how to keep the original? 
        # naively: copy array, use array as reference
        copy = nums.copy()
        n = len(nums)
        for i in range(len(nums)):
            newIndex = (i - k) % n
            nums[i] = copy[newIndex]
            


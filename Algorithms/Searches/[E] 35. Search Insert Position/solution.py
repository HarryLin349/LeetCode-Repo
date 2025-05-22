class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = floor((left + right) / 2)
        while ( left < right):
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left = mid + 1
            else:
                right = mid
            mid = floor((left + right) / 2) 
        return mid
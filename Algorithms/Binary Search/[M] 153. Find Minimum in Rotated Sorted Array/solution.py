class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # window closes in on possible min
        # idea: left will never exclude smaller vals
        # right will close to exclude larger vals
        count = 0
        while (left < right):
            mid = (left + right) // 2
            # print("window starts at", left, mid, right, ">", nums[left], nums[mid], nums[right])
            maxval = max(nums[left], nums[right], nums[mid])
            minval = min(nums[left], nums[right], nums[mid])
            minind = left if nums[left] == minval else right if nums[right] == minval else mid
            maxind = left if nums[left] == maxval else right if nums[right] == maxval else mid
            midind = (minind + maxind) // 2
            left = maxind + 1
            right = minind
            # print("window shrunk to L, R", maxind, minind, "vals", nums[maxind], nums[minind])
            if left > right:
                return nums[right]

        return nums[right]

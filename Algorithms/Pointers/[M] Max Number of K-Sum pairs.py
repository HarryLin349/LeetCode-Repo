class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # intuition 
        count = 0
        nums.sort()
        l, r = 0, len(nums) -1
        while (l < r):
            hod = nums[l] + nums[r] 
            if (hod == k):
                count += 1
                nums.pop(l)
                nums.pop(r -1)
                r -= 2
            elif (hod < k):
                # move left pointer up
                l += 1
            else:
                r -= 1
        return count
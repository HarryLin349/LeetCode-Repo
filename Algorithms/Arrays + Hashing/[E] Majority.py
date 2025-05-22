# 169. Majority Element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # brute force: keep track of counts in a dict 
        # select biggest
        # Time: O(n), space: O(n)
        # want: Time O(n), Space O(1)

        majority = nums[0]
        count = 0
        for i in range(len(nums)):
            if (count == 0):
                majority = nums[i]
                count += 1
            elif (majority == nums[i]):
                count += 1
            else:
                count -= 1
        return majority


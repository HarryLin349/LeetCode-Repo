class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            # check each start of sequence
            if (num - 1) not in numset:
                nextnum = num + 1
                while nextnum in numset:
                    nextnum += 1
                longest = max(longest, nextnum - num)
        return longest
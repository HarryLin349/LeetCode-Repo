class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = [-1] * n
        jumps[n-1] = 0
        for i in reversed(range(n -1)):
            cmin = jumps[i+1]
            indmax = min(i+nums[i], n-1)
            for j in range(i + 1, indmax + 1):
                cmin = min(cmin, jumps[j])
            jumps[i] = cmin + 1
        print(jumps)
        return jumps[0]
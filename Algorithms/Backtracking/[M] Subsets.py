class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # idea: recursively
        # backtracking, which is like DFS
        # iterate through every num in nums
        # for each, we either take in our curr subset or we don't
        result = []
        curSubset = []
        n = len(nums)

        def dfs(i):
            # i >= n? we've evaluated every elem in nums, can return our decision here now
            if i >= n:
                result.append(curSubset.copy())
                return
            # choice 1
            curSubset.append(nums[i])
            dfs(i+1)

            # choice 2
            curSubset.pop()
            dfs(i+1)
            return
        dfs(0)
        return result
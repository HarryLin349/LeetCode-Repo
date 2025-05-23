class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # for each elem, pick a random num from remaining
        result = []
        cur = []
        n = len(nums)

        def dfs(i):
            if (i >= n):
                # we've filled every spot
                result.append(cur.copy())
                return
            
            # for the current, add each remaining elem, and then return
            for j in range(n):
                if nums[j] not in cur:
                    cur.append(nums[j])
                    dfs(i+1)
                    cur.pop()
            return
        
        dfs(0)
        return result
    
'''
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # take each elem of nums
        # creating a permutation
        # pick one of the elems
            # remove it from the choices
            # repeat?
            # no duplicates (good)
        # first idea --> backtracking ? 
        
        answers = []

        def backtrack(cur):
            if (len(cur) == len(nums)):
                answers.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] not in cur: # O(n)
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
            
        backtrack([])
        return answers

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # idea: same as with subsets I except with duplicates
        # at each step we can either take or not take the element to add to the cur subset
        # issue: we shouldn't start the backtrack step to take the rest of the elems
        # if the cur elem is the same as the prev and len(cur) == 
        sortednums = sorted(nums)
        answers = []
        n = len(nums)
        def backtrack(i, cur):
            if (i == n):
                answers.append(cur[:])
                return
            # take
            cur.append(sortednums[i])
            backtrack(i+1, cur)
            cur.pop()

            # don't take
            # if we decide not to take nums[i], we skip all other instances of the num
            # since not taking this one but taking the next would essentially be the same as taking it
            while (i < n-1 and sortednums[i] == sortednums[i+1]):
                i += 1
            backtrack(i+1, cur)

                

        backtrack(0, [])
        return answers
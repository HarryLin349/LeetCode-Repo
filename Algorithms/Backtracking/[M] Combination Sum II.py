class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # backtracking --> maintain prev combinations
        # at each step, what choice can we make?
        # given at i, we can choose from i+1 .. n
        # --> ensures no duplicate indexes
        # but can't have duplicate answers either
        # set? List isn't hashable.. could use an n tuple but that seems wasteful
        # issue: I don't think there's a way to know if your solution is a duplicate until the very end
        # unless.. you can?
        # since we're going L to R, we can assume if answers already contains the value
        # it will be a duplicate

        # idea: try sorting? 
        # then we can
        answers = []
        candidates.sort()

        def backtrack(index, curList, total):
            if total == target:
                answers.append(curList[:])
            if total > target:
                return
            for i in range(index, len(candidates)):
                if (i > index and candidates[i] == candidates[i-1]):
                    continue
                curList.append(candidates[i])
                backtrack(i+1, curList, total+candidates[i])
                curList.pop()
        backtrack(0, [], 0)
        return answers
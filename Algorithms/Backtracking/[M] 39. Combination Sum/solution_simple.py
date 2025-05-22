class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answers = []
        n = len(candidates)

        def backtrack(index, curlist, total):
            # print(f"i: {index}, curlist: {curlist}")
            if (total == target):
                # print (f"curlist {curlist} sums to {target}")
                answers.append(copy.copy(curlist))
            elif total > target:
                return
            for i in range(index, n):
                curlist.append(candidates[i])
                backtrack(i,curlist, total + candidates[i])
                curlist.pop()
        backtrack(0, [], 0)
        return answers
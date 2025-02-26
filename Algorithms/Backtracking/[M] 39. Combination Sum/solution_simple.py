class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        n = len(candidates)

        def backtrack(index, curList, total):
            # print(f"i: {index}, curList: {curList}")
            if (total == target):
                # print (f"curList {curList} sums to {target}")
                answers.append(copy.copy(curList))
            elif total > target:
                return
            for i in range(index, n):
                curList.append(candidates[i])
                backtrack(i,curList, total + candidates[i])
                curList.pop()
        backtrack(0, [], 0)
        return answers
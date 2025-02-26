class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # idea: backtracking, we go through nums from 1-9
        # add answers if len(curList) = k and sum(curList) = n
        answers = []

        def backtrack(index, curList, total):
            if (total == n and len(curList) == k):
                answers.append(curList[:])
            if (total > n or len(curList) > k):
                return
            for i in range(index, 9):
                curList.append(i+1)
                backtrack(i+1, curList, total + i+1)
                curList.pop()
        backtrack(0,[],0)
        return answers
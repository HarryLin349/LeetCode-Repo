class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # idea: backtracking, we go through nums from 1-9
        # add answers if len(curlist) = k and sum(curlist) = n
        answers = []

        def backtrack(index, curlist, total):
            if (total == n and len(curlist) == k):
                answers.append(curlist[:])
            if (total > n or len(curlist) > k):
                return
            for i in range(index, 9):
                curlist.append(i+1)
                backtrack(i+1, curlist, total + i+1)
                curlist.pop()
        backtrack(0,[],0)
        return answers
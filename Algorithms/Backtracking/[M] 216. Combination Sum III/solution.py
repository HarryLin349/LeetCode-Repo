class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.res = []
        def backtrack(self, perm, k, n):
            if (len(perm) == k and sum(perm) == n):
                self.res.append([x for x in perm])
            start = 1 if len(perm) == 0 else perm[-1] + 1
            for i in range(start, 10):
                perm.append(i)
                backtrack(self, perm, k,n)
                perm.pop()
        backtrack(self, [], k,n)
        return(self.res)
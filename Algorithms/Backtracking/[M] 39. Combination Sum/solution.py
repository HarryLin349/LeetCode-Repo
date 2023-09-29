class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.tracked = []
        def backtrack(self, perm, freq, candidates, target):
            if (sum(perm) == target and freq not in self.tracked):
                self.res.append(list(perm))
                self.tracked.append(list(freq))
            elif (sum(perm) > target):
                return
            for i, num in enumerate(candidates):
                perm.append(num)
                freq[i] += 1
                backtrack(self, perm, freq, candidates, target)
                freq[i] -= 1
                perm.pop()
        backtrack(self, [], [0] * len(candidates), candidates, target)
        return self.res
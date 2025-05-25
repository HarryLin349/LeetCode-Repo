from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        seen = defaultdict(int)
        res = 0
        for domino in dominoes:
            d = (domino[0], domino[1])
            rev = (domino[1], domino[0])
            if seen[d]> 0 or seen[rev] > 0:
                res += seen[d]
                if d[0] != d[1]:
                    res += seen[rev]
            seen[d] += 1

        return res

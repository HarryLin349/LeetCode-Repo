from collections import defaultdict
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        '''
        ideas
        compare rows and columns
        naively, build a cols list
        and compare O(n^2*k)

        hashing?
        hash a row and a column
        '''
        seen = defaultdict(int)
        res = 0
        for i in range(len(grid)):
            seen[tuple(grid[i])] += 1
        for j in range(len(grid[0])):
            cur = []
            for i in range(len(grid)):
                cur.append(grid[i][j])
            if tuple(cur) in seen:
                res += seen[tuple(cur)]
        return res
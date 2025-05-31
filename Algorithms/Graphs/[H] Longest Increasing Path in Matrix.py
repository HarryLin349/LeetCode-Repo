from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        '''
        idea: backtracking
        start at each, explore 1 if we can, then undo the move
        issue is the potential start and end could be anywhere
        backtracking from each source would be O(m^2n^2, way too long)

        is there a way to do it while reusing info?
        start at maximum value of the matrix.
        we want the max distance.
            for neighbors, distance += 1 if its less than it

        maybe, for each tile, track if it has a neighbor UDLR greater than it (e.g. tuple)

        note that we can't have cycles, since strictly increasing
        so we have a directed acyclic graph
        in a directed acyclic graph, find the longest path.
        probably just do topological sort on each element
        '''

        distance = defaultdict(int)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(matrix), len(matrix[0])

        def dfs(i,j):
            dist = 1
            nextdist = 0
            if (i,j) in distance:
                return distance[(i,j)]
            # explore all neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (ni >= 0 and ni < m and nj >=0 and nj < n):
                    if (matrix[ni][nj] > matrix[i][j]):
                        nextdist = max(nextdist, dfs(ni,nj))
            # then mark self distance from dist + max of neighbors
            dist += nextdist
            distance[(i,j)] = dist
            return distance[(i,j)]
            # and return
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res
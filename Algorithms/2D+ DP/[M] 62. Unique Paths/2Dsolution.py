class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # paths[i][j] -> num paths that lead to i,j
        paths = [[-1 for _ in range(n)] for _ in range(m)]
        paths[0][0] = 0
        i,j = 0,0
        for i in range(m):
            for j in range(n):
                top, left = 0, 0
                if (i > 0):
                    top = paths[i-1][j]
                if (j > 0):
                    left = paths[i][j-1]
                paths[i][j] = max(1,top + left)
        print(paths[m-1][n-1])
        return paths[m-1][n-1]
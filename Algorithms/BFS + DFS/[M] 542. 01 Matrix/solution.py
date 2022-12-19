class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = mat
        for r in range(m):
            for c in range(n):
                if (mat[r][c] == 0):
                    result[r][c] = 0
                else:
                    top = result[r -1][c] if r > 0 else m+n+1
                    left = result [r][c -1] if c > 0 else m+n+1
                    result[r][c]= min(top + 1,left + 1)        
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if (mat[r][c] == 0):
                    result[r][c] = 0
                else:
                    bot = result[r + 1][c] if r < m -1 else m+n+1
                    right = result [r][c +1] if c < n-1 else m+n+1
                    result[r][c]= min(result[r][c],bot + 1,right + 1)
        return result

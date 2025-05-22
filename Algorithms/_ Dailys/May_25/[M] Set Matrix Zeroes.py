'''
Employs hashing strategies
'''
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        naively, scan through once to get a set of zeroes
        then, set the cols and rows with those to zero
        """
        zeroes = set()
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroes.add((i,j))
        
        for row, col in zeroes:
            for i in range(n):
                matrix[i][col] = 0
            for j in range(m):
                matrix[row][j] = 0
        
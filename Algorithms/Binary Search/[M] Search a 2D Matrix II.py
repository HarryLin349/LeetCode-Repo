class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # naively: binsearch every row O(mlogn)
        # what math properties can we see here?
        # increasing diagonals
        # 1: tl > br
        # 2: l<r, t < b
        # 3: r+, d+, l-, t-

        # corners: tl < bl ? tr < br
        # idea: start at top left
        # if target > cur, two options
        # if target > next diag, cur = next diag

        # idea: start at top left
        # why? l>r you can grow in either direction (ambigious)
        # r -> l always smaller
        # t -> b always bigger
        # if target < cur, move left
        # if target > cur, move down

        m,n = len(matrix) - 1, len(matrix[0]) - 1
        cr,cc = 0,n
        while (cr <= m and cc >= 0):
            val = matrix[cr][cc]
            if target > val:
                cr += 1
            elif target < val:
                cc -= 1
            else:
                return True
        return False
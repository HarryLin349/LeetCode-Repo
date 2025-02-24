class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time complexity --> halve candidates each time
        # traditional binary search:
        # l,r, mid, and you keep halving the target space
        # idea: binsearch on y axis, then the x axis?
        # first, search for matching row
        top,bottom,mid = 0, len(matrix) - 1, 0
        counter = 0
        while top <= bottom and counter < 10:
            mid = (top + bottom) // 2
            counter += 1
            val = matrix[mid][0]
            if target < val:
                bottom = mid - 1
            elif target > val:
                top = mid + 1
            else:
                return True

        if matrix[mid][0] > target:
            mid -= 1
        print (f"val is probably in row {mid} between {matrix[mid][0]} and {matrix[mid][-1]}")
        # if we're here, we can search the mid row now
        l,r,midcol = 0, len(matrix[mid]) - 1, 0
        while l <= r:
            midcol = (l+r) // 2
            val = matrix[mid][midcol]
            if target < val:
                r = midcol - 1
            elif target > val:
                l = midcol + 1
            else:
                return True
        return False
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        copy = grid
        maxCount = 0
        m = len(copy)
        n = len(copy[0])

        def findCount(x,y) -> int:
            nonlocal copy, m
            count = 0
            queue = [(x,y)]
            perms = [(-1, 0), (1,0), (0,-1), (0,1)]
            for r, c, in queue:
                if (copy[r][c] == 1):
                    count += 1
                    copy[r][c] = 2
                else:
                    continue
                for rx, ry in perms:
                    if (r + rx) < m and (r + rx) >= 0 and (c + ry) < n and (c+ ry) >= 0:
                        if (copy[r+rx][c+ry] == 1):
                            queue.append((r+rx, c+ry))
            return count
            
        for x in range (len(copy)):
            for y in range (len(copy[0])):
                if copy[x][y] == 1:
                    count = findCount(x,y)
                    if count > maxCount:
                        maxCount = count
        return maxCount

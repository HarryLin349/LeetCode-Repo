from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        distances = grid
        queue = deque([])
        perms = [(-1, 0), (1,0), (0,-1), (0,1)]
        minutes = 0
        freshCount = 0
        for r in range(m):
            for c in range(n):
                if (distances[r][c] == 2):
                    distances[r][c] = 0
                    queue.append((r,c))
                elif distances[r][c] == 1:
                    freshCount += 1
                    distances[r][c] = -1
                elif distances[r][c] == 0:
                    distances[r][c] = -2
        while queue:
            r,c = queue.popleft()
            for x,y in perms:
                newx, newy = r+x, c+y
                if (newx >= 0 and newx < m and newy >= 0 and newy < n and distances[newx][newy] == -1):
                    distances[newx][newy] = distances[r][c] + 1
                    freshCount -= 1
                    if (distances[r][c] + 1 > minutes):
                        minutes = distances[r][c] + 1
                    queue.append((newx,newy))
        return minutes if freshCount == 0 else -1

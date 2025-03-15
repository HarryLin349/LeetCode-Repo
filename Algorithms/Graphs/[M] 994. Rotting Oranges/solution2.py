class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # idea: explore BFS wise, marking oranges as rotten with each iteration
        # keep track of time with each iterations
        #
        
        # first, count oranges
        fresh_oranges = 0
        queue = []
        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(grid), len(grid[0])
        minDist = [[m * n] * n for _ in range(m)]

        # Count oranges, queue starting positions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    minDist[i][j] = 0
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while queue:
            ci, cj = queue.pop(0)
            if grid[ci][cj] == 1:
                fresh_oranges -= 1 # increase our infection count

            grid[ci][cj] = 2
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (ni >= 0 and ni < m and nj >=0 and nj < n and grid[ni][nj] == 1):
                    queue.append((ni, nj))
                    minDist[ni][nj] = min(minDist[ci][cj] + 1, minDist[ni][nj])
                    time = max(time, minDist[ni][nj])

        # print (f"time {time} fresh_oranges {fresh_oranges}")
        # print(minDist)

        return time if fresh_oranges == 0 else -1
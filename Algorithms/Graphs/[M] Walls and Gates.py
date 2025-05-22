class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        INF = 2147483647
        # idea: start with BFS from each treasure chest
        # queue filled with (pos, distance)?
        # on each iter, set distance of land tiles to the cur distance
        # traverse to neighbors if:
        # not water (not -1)
        # not treasure (not 0)
        # neighbor value is > cur distance + 1

        queue = []
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])

        # find all the treasure chests
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j, 0))
        print(f"starting queue: {queue}")
        
        #now, BFS from treasure chests to land
        while queue:
            ci, cj, dist = queue.pop(0)
            if (grid[ci][cj] >= 0 and dist <= grid[ci][cj]):
                # print(f"changed {ci} {cj} to {dist}!")
                grid[ci][cj] = dist
            else:
                continue
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (ni >= 0 and ni < m and nj >= 0 and nj < n):
                    queue.append((ni, nj, dist + 1))

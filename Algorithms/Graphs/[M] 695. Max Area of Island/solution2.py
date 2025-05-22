class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea = 0
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        # idea: iterate over
        # when we get an island, run "getIslandArea" which
        # bfs the island (zeroing it out) and returns the area
        print(grid)
        def getIslandArea(i,j):
            area = 0
            queue = [(i,j)]
            while queue:
                ci, cj = queue.pop(0)
                if (ci < 0 or ci >= m or cj < 0 or cj >= n or grid[ci][cj] == 0):
                    continue
                grid[ci][cj] = 0
                area += 1
                for ni, nj in directions:
                    newi, newj = ci + ni, cj + nj
                    queue.append((newi, newj))
            return area

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    carea = getIslandArea(i,j)
                    print (f"island at {i} {j} with area {carea}")
                    maxArea = max(maxArea, carea)
        return maxArea

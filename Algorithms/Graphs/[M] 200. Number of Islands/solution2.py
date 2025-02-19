class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # idea: iterate over each space in the grid
        # when encountering a 1, increment numIslands by 1
        # then, fill it out with BFS, turning each 1 into a 0
        numi = 0
        n,m = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    numi += 1
                    # explore with bfs
                    queue = [(i,j)]
                    while queue:
                        ci, cj = queue[-1]
                        grid[ci][cj] = "0"
                        queue.pop()
                        for ni, nj in directions:
                            newi, newj = ci + ni, cj + nj
                            if (newi < 0 or newi >= n or newj < 0 or newj >= m or grid[newi][newj] == "0"):
                                continue
                            queue.append((newi, newj))
        return numi 

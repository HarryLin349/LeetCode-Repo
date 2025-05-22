class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        moves = [(0,1), (0, -1), (1,0), (-1,0)]
        # keep track of islands
        # BFS from origin, when we encounter a 1:
        #   increment the number of islands
        #   fill in all adj. 1s as 0s 
        def zeroIsland(r,c):
            queue = [(r,c)]
            while (queue):
                cx,cy = queue.pop(0)
                for x, y in moves:
                    nx = cx + x
                    ny = cy + y
                    if (nx >= 0 and nx < len(grid) and ny >=0 and ny < len(grid[0])):
                        if grid[nx][ny] == "1":
                            queue.append((nx,ny))
                            grid[nx][ny] = "0"

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    zeroIsland(r,c)
                    islands += 1
        return islands

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        valid = []
        def checkFlood(r,c,n,m)-> bool:
            visited = []
            queue = [(r,c)]
            moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
            reachedPacific, reachedAtlantic = False, False
            while (queue):
                cx, cy = queue.pop(0)
                if [cx, cy] in valid:
                    return True
                if cx == 0 or cy == 0:
                    reachedPacific = True
                if cx == n - 1 or cy == m - 1:
                    reachedAtlantic = True
                for x, y in moves:
                    nx, ny = cx + x, cy + y
                    if (nx >= 0 and nx < len(heights) and ny >=0 and ny < len(heights[0])):
                        if (heights[nx][ny] <= heights[cx][cy]) and (nx,ny) not in visited:
                            queue.append((nx,ny))
                            visited.append((nx,ny))
            return reachedPacific and reachedAtlantic
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                result = checkFlood(r,c,len(heights), len(heights[0]))
                if result:
                    valid.append([r,c])
        return valid
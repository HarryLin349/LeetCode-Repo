class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # idea: work in reverse? 
        # have pacific and atlantic
        # BFS from edges, if the neighbor is >= then visit it (set to True)

        m,n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        q = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # fill pacific ocean
        for col in range(n):
            q.append((0,col))
        for row in range(1,m):
            q.append((row,0))
        
        while q:
            ci, cj = q.pop(0)
            pacific[ci][cj] = True
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (ni >= 0 and ni < m and nj >= 0 and nj < n and pacific[ni][nj] == False and heights[ni][nj] >= heights[ci][cj]):
                    q.append((ni,nj))
    
        q = []
        # fill atlantic ocean
        for col in range(n):
            q.append((m-1, col))
        for row in range(m-1):
            q.append((row, n-1))
        
        while q:
            ci, cj = q.pop(0)
            atlantic[ci][cj] = True
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if (ni >= 0 and ni < m and nj >= 0 and nj < n and atlantic[ni][nj] == False and heights[ni][nj] >= heights[ci][cj]):
                    q.append((ni,nj))
        
        results = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    results.append([i,j])
        return results
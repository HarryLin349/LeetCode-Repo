from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        '''
        idea: for each gate, run bfs from it and update distances
        can probably update distance in place, only update if its <= cur
        '''
        INF = 2**31 - 1
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            i,j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (ni >= 0 and ni < m and nj >=0 and nj < n and rooms[ni][nj] != -1):
                    if (rooms[i][j] + 1 < rooms[ni][nj]):
                        rooms[ni][nj] = rooms[i][j] + 1
                        queue.append((ni,nj))

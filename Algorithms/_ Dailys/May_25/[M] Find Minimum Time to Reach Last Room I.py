from collections import deque
from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        '''
        nxm rooms in a grid
        min time to reach n-1, m-1
        moving takes 1s
        can only enter a room if moveTime <= curTime

        ideas: greedy? move to the room with least moveTime... probably not good
        note that we want to move down or right every time, no point going backwards

        doesnt work

        0 1 5 
        2 5 5
        1 1 X

        ideas: count backwards? bfs from goal
        tile's time is 1 + min(right, down)
        doesnt seem to work.. if final room is 2s wait we dont necessarily need to wait that much
        only add a rooms wait time if its greater than the cur? 
        
        explore via min wait Time .. 
        for each next move, calculate distance(new, new) as distance(source) + 1 or its wait time +1
            for each, pendingTime = max(moveTime[i][j], prev) + 1 <- either how long it took or the wait time (larger)
            totalTime[i][j] = min(totalTime[i][j], pendingTime)
        '''
        n,m = len(moveTime), len(moveTime[0])
        MAX = 10**9 + n * m + 1
        totalTime = [[MAX for _ in range(m)] for _ in range (n)]
        totalTime[0][0] = 0
        q = [(0,0,0)]
        moves = [(1,0), (-1, 0), (0,1), (0,-1)] 
        counter = 0
        visited = set()
        while q:
            # counter += 1
            time,i,j = heappop(q)
            visited.add((i,j))
            if i == n -1 and j == m -1:
                break
            # print(f"cur at {i} {j}, time: {time}, q: {len(q)}")
            # check right
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if (ni >= 0 and ni < n and nj >=0 and nj < m):
                    if (ni, nj) in visited or totalTime[ni][nj] <= time + 1:
                        continue
                    pendingTime = max(moveTime[ni][nj], time) + 1
                    totalTime[ni][nj] = min(totalTime[ni][nj], pendingTime)
                    heappush(q, (totalTime[ni][nj], ni, nj))
        # for row in totalTime:
        #     print(row)
        return totalTime[n-1][m-1]

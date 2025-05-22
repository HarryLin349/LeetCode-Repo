from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        '''
        ideas:
        least cost path, where the cost of the next dest is
        curCost = 1 or 2
        pendingTime = max(moveTime(dest), curTime) + curCost
        totalTime(dest) = min (totalTime(dest), pendingTime) 
        simply add on to the tuple with the cost of the nextMove 
        '''
        # time, cost, i, j
        n,m = len(moveTime), len(moveTime[0])
        q = [(0,1,0,0)]
        visited = set()
        MAX = 10**9 + n*m + 1 
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        totalTime = [[MAX for _ in range(m)] for _ in range(n)]
        totalTime[0][0] = 0
        while q:
            time, cost, i,j = heappop(q)
            visited.add((i,j))
            # explore in all
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if (ni >= 0 and ni < n and nj >=0 and nj < m):
                    if (ni,nj) in visited or totalTime[ni][nj] <= max(moveTime[ni][nj], time) + cost:
                        continue
                    pendingTime = max(moveTime[ni][nj], time) + cost
                    totalTime[ni][nj] = min(totalTime[ni][nj], pendingTime)
                    newCost = 2 if cost == 1 else 1
                    heappush(q, (totalTime[ni][nj], newCost, ni, nj))
        return totalTime[n-1][m-1]

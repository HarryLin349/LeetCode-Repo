from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        precompute counts of each grid (if mine, set all around it to += 1)
        then traverse via BFS from click:
            - if mine, set to X and return
            - if empty (0) change to B and add all neighbors to queue
            - if nonempty reveal and dont add neighbors to q
        '''
    
        curboard = board
        cc, cr = click[0], click[1]
        if board[cc][cr] == "M":
            curboard[cc][cr] = "X"
            return curboard
        m,n = len(board), len(board[0])
        counts = [[0 for _ in range(n)] for _ in range (m)]
        perms = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1),(1,-1), (1,0), (1,1)]
        for i in range (m):
            for j in range(n):
                if board[i][j] == "M":
                    for di, dj in perms:
                        ni, nj = i + di, j + dj
                        if ni >= 0 and ni < m and nj >= 0 and nj < n:
                            counts[ni][nj] += 1
                    counts[i][j] = -1
        queue = deque([(cc, cr)])
        while queue:
            ci, cj = queue.popleft()
            if curboard[ci][cj] != "E":
                # don't explore already explored
                continue
            if counts[ci][cj] == 0:
                # set cur to B
                curboard[ci][cj] = "B"
                # explore neighors
                for di, dj in perms:
                    ni, nj = ci + di, cj + dj
                    if ni >= 0 and ni < m and nj >= 0 and nj < n:
                        queue.append((ni, nj))
            elif counts[ci][cj] > 0:
                # set cur to its count and stop exploring
                curboard[ci][cj] = str(counts[ci][cj])
        return curboard


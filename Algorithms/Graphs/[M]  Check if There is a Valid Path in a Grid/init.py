from enum import Enum
class Solution:
    '''
    Idea: Iteratively explore (BFS?) tiles to surrounding tiles to determine if reachable
    could also construct a DAG?
    Need context, e.g. 3->5 is only valid if youre travelling down 
    Or maybe represent each port as bools? e.g. street 1 is UDLR FFTT
    at each tile, iterate over each direction UDLR
    if direction == Down and street = 5, valid
    Have a set of directions for each street that are valid? e.g. valid moves into it

    so psuedocode:
    curpos = (0,0)
    visited = ...
    while True: 
        if curPos = end, return True
        for dir in direction:
            if direction in validDirections[street]:
                update curPos, break
    '''

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = [0,1,2,3] # UDLR
        validOutput = {
            1: set([2,3]),
            2: set([0,1]),
            3: set([1,2]),
            4: set([1,3]),
            5: set([0,2]),
            6: set([0,3]),

        }
        validInput = {
            1: set([2,3]),
            2: set([0,1]),
            3: set([0,3]),
            4: set([0,2]),
            5: set([1,3]),
            6: set([1,2]),
        }
        curPos = (0,0)
        m,n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
        directions = [(-1,0), (1,0), (0,-1), (0,1)] # UDLR
        queue = [curPos]
        while queue:
            i,j = queue.pop(0)
            visited[i][j] = True
            if i == m-1 and j == n-1:
                return True
            stuck = True
            street = grid[i][j]
            for dir, dirTuple in enumerate(directions):
                if dir not in validOutput[street]:
                    continue
                di,dj = dirTuple
                ni, nj = i+di, j + dj
                if ni >= 0 and ni < m and nj >=0 and nj< n and not visited[ni][nj]: # if direction is within grid
                    newStreet = grid[ni][nj]
                    if dir in validInput[newStreet]:
                        queue.append((ni,nj))
        return False

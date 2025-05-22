class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(board), len(board[0 ])
        def backtrack(curPos, curInd, visited):
            if curInd == len(word) - 1:
                return True
            ci,cj = curPos
            ans =  False
            for di,dj in directions:
                ni,nj = ci+di, cj+dj
                if (ni, nj) in visited:
                    continue
                if (ni >= 0 and ni < m and nj >= 0 and nj < n):
                    if board[ni][nj] == word[curInd + 1]:
                        visited.add((ci,cj))
                        ans = ans or backtrack((ni,nj), curInd + 1, visited)
                        visited.remove((ci, cj))
            return ans
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack((i,j), 0, set()):
                    return True
        return False


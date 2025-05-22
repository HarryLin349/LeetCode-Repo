class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        moves = [(0,1), (0, -1), (-1, 0), (1,0)]
        self.res = False
        def search(ind, cx,cy, visited):
            if ind >= len(word):
                self.res = True
                return
            for i in range (4):
                x, y = moves[i]
                nx, ny = cx + x, cy + y
                if nx >= 0 and nx < len(board) and ny >=0 and ny < len(board[0]):
                    if (board[nx][ny] == word[ind]) and (nx,ny) not in visited:
                        visited.append((nx,ny))
                        search(ind + 1, nx,ny, visited)
                        visited.pop()
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if len(word) == 1:
                        return True
                    search(1,x,y,[(x,y)])
                    if self.res:
                        return True
        return False
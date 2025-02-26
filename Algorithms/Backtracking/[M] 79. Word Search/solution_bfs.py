class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # naively: for each start point, BFS to search the words around it
        # runtime: O(mn) * O(4^n)
        seen = set()
        queue = []
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def explore(i,j,num):
            if (num >= len(word) -1):
                return True
            seen.add((i,j))
            ans = False
            for x,y in directions:
                newx, newy = i + x, j + y
                if (newx >= 0 and newx < m and newy >= 0 and newy < n):
                    if board[newx][newy] == word[num + 1] and (newx, newy) not in seen:
                        ans = ans or explore(newx,newy, num + 1)
            seen.remove((i,j))
            return ans


        for i in range(m):
            for j in range(n):
                if (board[i][j] == word[0] and (i,j) not in seen):
                    if explore(i,j,0):
                        return True
                    seen = set()
        return False
        

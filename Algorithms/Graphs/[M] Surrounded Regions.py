class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # observation: every O cell is a region unless its connected to the edge of the board
        # idea: first check edges
        # if O, run a fill algorithm to change O -> "E" and storing the coords in an edges array
        # then iterate over the board, filling all O to 
        # lastly, for each coord in edge fill the E to O
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        n, m = len(board), len(board[0])
        
        def fillAtoB(startingcoords, A,B):
            queue = [startingcoords]
            while queue:
                cx,cy = queue.pop()
                board[cx][cy] = B
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != A:
                        continue
                    queue.append((nx, ny))
        
        # iterate over the edges of the board
        edges = []
        # top and bottom rows
        for i in range(m):
            if board[0][i] == "O":
                fillAtoB((0,i), "O", "E")
                edges.append((0,i))
            if board[n-1][i] == "O":
                fillAtoB((n-1,i), "O", "E")
                edges.append((n-1,i))


        # left and right edges
        for i in range(n):
            if board[i][0] == "O":
                fillAtoB((i,0), "O", "E")
                # edges.append((i,0))
            if board[i][m-1] == "O":
                fillAtoB((i,m-1), "O", "E")
                # edges.append((i,m-1))

        # now we can iterate over and check for islands (skip the edges)
        # for i in range(1, n-1):
        #     for j in range(1, m-1):
        #         if board[i][j] == "O":
        #             fillAtoB((i,j), "O", "X")
        
        # for i,j in edges:
        #     fillAtoB((i,j), "E", "O")

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
        
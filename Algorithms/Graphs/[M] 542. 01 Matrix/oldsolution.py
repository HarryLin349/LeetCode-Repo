    def findClosestZero(self, x,y,m,n, grid):
        perms = [(1,0), (0,1)]
        queue = [(x,y)]
        visited = []
        for r,c in queue:
            visited.append((r,c))
            for mx, my in perms:
                newx = r+mx
                newy= c+my
                if (newx) < m and (newx) >= 0 and (newy) < n and (newy) >= 0:
                    if (grid[newx][newy]) == 0:
                        # return count
                        return abs(newx - x) + abs(newy - y)
                    elif (newx, newy) not in visited:
                        queue.append((newx,newy))
        return m + n + 1

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        result = mat
        for x in range(m):
            for y in range(n):
                if (mat[x][y] == 0):
                    result[x][y] = 0
                else:
                    a,b,c= m+n +1, m+n +1, m+n +1 
                    if (x != 0):
                        a=result[x-1][y] + 1
                    if (y!=0):
                        b = result[x][y-1] + 1
                    c = self.findClosestZero(x,y,m,n,mat)
                    result[x][y] = min(a,b,c)
        return result


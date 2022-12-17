class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        copy = image
        if color == og: return copy
        queue = [(sr, sc)]
        m = len(image)
        n = len(image[0])
        perms = [(-1, 0), (1,0), (0,-1), (0,1)]
        for r, c in queue:
            copy[r][c] = color
            for x,y in perms:
                if (r + x) < m and (r + x) >= 0 and (c + y) < n and (c+y) >= 0:
                    if (copy[r+x][c+y] == og):
                        queue.append((r+x, c+y))
        return copy

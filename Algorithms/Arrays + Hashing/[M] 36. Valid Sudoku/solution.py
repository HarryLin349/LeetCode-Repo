class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenrows = [[0]*9 for i in range (9)]
        seencols = [[0]*9 for i in range (9)]
        seengrids = [[0]*9 for i in range (9)]
        for i in range(9):
            for j in range(9):
                gridnum = 3 * (i // 3) + (j // 3)
                if board[i][j] != ".":
                    val = int(board[i][j]) - 1
                    if seenrows[i][val] == 1 or seencols[j][val] == 1 or seengrids[gridnum][val] == 1:
                        return False
                    seenrows[i][val] = 1
                    seencols[j][val] = 1
                    seengrids[gridnum][val] = 1
        return True

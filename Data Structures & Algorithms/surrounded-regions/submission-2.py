class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # If cell is out of bounds or if cell is not O, just return.
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        # If any bordering cell is 'O', perform DFS on it.
        for row in range(ROWS):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][COLS - 1] == 'O':
                dfs(row, COLS - 1)

        for col in range(COLS):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[ROWS - 1][col] == 'O':
                dfs(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        
# GOAL
# ========
# Given an m x n matrix of Xs nd Os, "capture" surrounding
# regions of Os (not on the edge) by replacing regions
# with Xs.

# IDEA
# ========
# * To start on Os, rather than to traverse by Xs.
# * Use dfs on each O cell, and check to see if any O
#   (or path) reaches an edge. If any path does, the
#   entire region is not enclosed, so we can't surround.
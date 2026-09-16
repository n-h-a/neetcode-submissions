class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if c < 0 or r < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r       , c - 1)
            dfs(r - 1   , c)
            dfs(r       , c + 1)
            dfs(r + 1   ,c)

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)
        return count

# GOAL
# =======
# Given a 2D grid where '1' represents land and '0'
# represents water, count and return the # of islands.

# An island is formed by connecting adjacent lands
# horizontally or vertically.

# IDEA
# =======
# Traverse the grid from top -> bottom and left -> right.
# If it is land, increment count and find all land it's 
#   connected to using dfs and change to water.
# If it is water, ignore.
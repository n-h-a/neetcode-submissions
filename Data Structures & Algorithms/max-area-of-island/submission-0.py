class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + (
                dfs(r, c - 1) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r + 1, c)
            )

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area
        

# GOAL
# =======
# Given a matrix, grid, where grid[i] is either a 0 ('land')
# or 1 'water', return the max area of an island in grid s.t.
# an island is a group of 1s connected horizontally or vertically.

# IDEA
# =======
# Use dfs to go though islands and find the area for each. Keep
# track of the max.
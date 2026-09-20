class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or 
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Process Pacific border cells
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])

        # Process Atlantic border cells
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

# GOAL
# =======
# Given a grid of heights above sea level s.t. the Pacific
# Ocean borders the top and left sides and the Atlantic
# Ocean borders the bottom and right sides, return a list
# of cells where water can flow from that cell to both the
# oceans.

# IDEA
# ========
# Use DFS on each cell. 
#   Check to see if any path reaches Pacific Ocean and if 
#       any path reaches Atlantic Ocean.
#   If any path reaches a dead end, return None.
# TC: O(N * 4^N)

# Use DFS/BFS on border cells.
#   From Pacific, see what other cells can reach Pacific.
#   From Atlantic, see what other cells can reach Atlantic.
# Return the cells that can reach BOTH.
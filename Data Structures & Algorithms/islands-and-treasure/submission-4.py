class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                n_r = r + dx
                n_c = c + dy

                # If not in grid, continue.
                if n_r < 0 or n_c < 0 or n_r >= ROWS or n_c >= COLS:
                    continue

                # Set the level of cell to +1 its parent.
                if grid[n_r][n_c] == INF:
                    grid[n_r][n_c] = grid[r][c] + 1
                    queue.append((n_r, n_c))




        # For each chest cell, perform one iteration of bfs.
        #   How do we know how many iterations of bfs per chest cell? If they have something in their queue.



# [
#   [&,-1,0, &],
#   [&, &,&,-1],
#   [&,-1,&,-1],
#   [0,-1,&, &]
# ]


# Fron each chest, I want to search all neighboring lands and their children. Use a queue to do BFS and find min distance through levels.


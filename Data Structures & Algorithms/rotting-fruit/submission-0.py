class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        minutes = 0

        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        while fresh > 0 and queue:
            # Freeze the queue length so you can determine # of minutes.
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nr = r + dx
                    nc = c + dy

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    
                    if grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1

# GOAL
# =======
# Given a grid that has fresh fruit (1), rotten fruit (2), and
# empty cells (0), return the min # of min it takes until
# all fruits are rotten. Every min, a fresh fruit becomes rotten
# if it is next to a rotten fruit.

# IDEA
# =======
# Use BFS starting from each fruit. Why? Because BFS helps us mark
# neighboring fruits. Each level can represent a minute, and the
# total # of levels == min # of minutes.
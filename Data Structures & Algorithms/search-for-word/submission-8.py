class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def explore(r, c, i):
            if (r, c) in visited or board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            visited.add((r, c))

            found = (
                (r > 0 and explore(r - 1, c, i + 1))
                or (c > 0 and explore(r, c - 1, i + 1))
                or (c < len(board[0]) - 1 and explore(r, c + 1, i + 1))
                or (r < len(board) - 1 and explore(r + 1, c, i + 1))
            )

            visited.remove((r, c))
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if explore(r, c, 0):
                    return True

        return False

# GOAL
# ========
# Given a 2D grid of chars and a word, return True if
# the word is in the grid. Otherwise, return false.

# IDEA
# ========
# Use backtracking to explore paths from letters in word.
# From a matching letter:
#       1) Explore up
#       2) Explore left
#       3) Explore right
#       4) Explore down
# Define a recursive function, explore(r, c, i):
#   If we already visited this cell or if the letters aren't same,
#       then return False. This path is not good.
#   If we're at the last letter and letts are the same, return True.
#   Otherwise,
#       Add current cell to visited.
#       Explore all possible paths:
#           Up, left, right, down.
#       Remove current cell from visited.
#       If any one of them return true, return true. Otherwise, false.
# Loop through every letter in board and run explore. Return true if
# any return True.
# TC: O(R * C * 4^L)
# SC: O(L)
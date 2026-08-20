class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                
                if elem == ".":
                    continue

                if elem in rows[i]:
                    return False
                rows[i].add(elem)

                if elem in cols[j]:
                    return False
                cols[j].add(elem)

                box_num = (i // 3) * 3 + (j // 3)
                if elem in boxes[box_num]:
                    return False
                else:
                    boxes[box_num].add(elem)

        return True
        

# GOAL
# =========
# Return true if Sudoku board is valid. Otherwise false.
# TC: O(N^2), SC: O(N^2)

# IDEA
# =========
# Have three dictionaries: One for rows, one for cols, one for sub-boxes.
# Loop through tiles:
#   Check if element is in row yet.
#       If yes, return False. Otherwise, add.
#   Check if element is in col yet.
#       If yes, return False. Otherwise, add.
#   Check if element is in sub-box yet.
#       If yes, return False. Otherwise, add.
# TC: O(N^2)
# SC: O(N^2)
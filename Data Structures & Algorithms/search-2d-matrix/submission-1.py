class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        lo = 0
        hi = N * M - 1

        while lo <= hi:
            midpoint = lo + (hi - lo) // 2

            row = midpoint // M
            col = midpoint % M

            elem = matrix[row][col]
            if elem == target:
                return True
            elif elem > target:
                hi = midpoint - 1
            else:
                lo = midpoint + 1

        return False

# GOAL
# ========
# Return true if target exists within matrix. 
# Otherwise, return false.

# BRUTE FORCE
# ========
# For each row,
#   For each column,
#       If element at row and column is target, return true.
# Return false if none found.
# TC: O(N * M)
# SC: O(1)

# IDEA
# ========
# Because the matrix is sorted in non-decreasing order, we know that:
#   if we pick an element and target is less than it, 
#       the target must be an element before and/or above it.
#   elif we pick an element and target is greater than it,
#       the target must be an element after and/or below it.
# Idea -- Use binary search.
#   How do we find the midpoint?
#       Find midpoint between lo and hi.
#       To get the row:
#           midpoint // M
#       To get the col:
#           midpoint % M
#   If element at midpoint < target,
#       Move lo to midpoint + 1
#   elif element at midpoint > target
#       Move hi to midpoint - 1
#   else, return true.

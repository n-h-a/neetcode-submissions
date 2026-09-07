class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        total = 0

        candidates.sort()
        def dfs(i):
            nonlocal total

            if target == total:
                res.append(combo.copy())
                return
            
            if i >= len(candidates) or total + candidates[i] > target:
                return

            combo.append(candidates[i])
            total += candidates[i]
            dfs(i + 1)

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            combo.pop()
            total -= candidates[i]
            dfs(i + 1)
        
        dfs(0)
        return res

# GOAL
# ========
# Given an array of ints (which may contain dups) and a target,
# return a list of all unique combos that add up to target.
# Each element can only be used at most once.

# IDEA
# ========
# Use backtracking: For each index, consider two possibilities:
#   1) Including the element
#   2) Not including the element
# Initialize arrays to store result and combination.
# Initialize variable to store total.
# Sort the arrays.
#   To prune branches early AND to skip dups with ease.
# Define a recursive function dfs(i):
#   If total == target,
#       Add copy of combo to result, then return early.
#   If considering past last index or total + nums[i] > target, return early.
#   Otherwise,
#       Add nums[i] to combo and perform dfs on next index with it.
#       
#       Skip past all the dups.
#       
#       Pop nums[i] from combo and perform dfs on next index without it.
# TC: O(N ^ 2*N)
# SC: O(N)
# Why does skipping past the dups handle our requirement for uniqueness?
#   When you do dfs on the first occurrence of an element and consider the path
#   that excludes it, the path already explores the same paths the dups would
#   explore. Because it handles that already, so we don't need to do dfs on dups.


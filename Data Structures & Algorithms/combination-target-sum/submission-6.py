class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        total = 0

        nums.sort()
        def dfs(i):
            nonlocal total

            if total == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or total + nums[i] > target:
                return

            combo.append(nums[i])
            total += nums[i]
            dfs(i)

            combo.pop()
            total -= nums[i]
            dfs(i + 1)

        dfs(0)
        return res
    
# GOAL
# =======
# Given an array of distinct ints and a target, return a list
# of all unique combos that sum to target. Can use the same 
# element multiple times.

# OBSERVATION
# =======
# * Can't use greedy because we want to consider all
#   possible combos; greedy picks best, then blocks.
# * To build all possible combos, we can use backtracking.

# IDEA
# =======
# Use backtracking: For each element, we consider 2 possibilities:
#   1) Include the element (again)
#   2) Do not include the element and move forward
# Initialize arrays for result and combo.
# Initialize variable for total.
# Sort the array to prune branches earlier
#   (If including element exceeds target, don't consider paths from there).
# Define the recursive function dfs(i):
#   If total == target:
#       Add copy of combo to result and return early.
#   If considering past last index or total + nums[i] > target:
#       Return early.
#   Otherwise,
#       Add number to combo and perform dfs on same index to consider
#       element again.
#       Then, pop number from combo and perform dfs on next index to
#       not consider element again.
# Perform dfs on 0 and return res.
# TC: O(N * 2^N)
# SC: O(N)

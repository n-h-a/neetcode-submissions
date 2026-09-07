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
#   1) Include the element and stay at the same index
#   2) Do not include the element and move forward
# Initialize arrays for result and combo.
# Sort the array to prune branches earlier
#   (If including element exceeds target, don't consider paths from there).
# Define the recursive function dfs(i, total):
# 
# 

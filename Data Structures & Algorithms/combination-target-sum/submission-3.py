class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or total + nums[i] > target:
                return

            combo.append(nums[i])
            dfs(i, total + nums[i])

            combo.pop()
            dfs(i + 1, total)

        dfs(0, 0)
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
# 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
        

# GOAL
# ========
# Given a list of ints which may contain dups and a target,
# return a list of unique combos that add up to target. Each
# element can only be used at most once in a combo.

# OBSERVATIONS
# ========
# * Unlike previous one, can't use same element more than once.
# * Seems like index matters a lot though.
# * The issue seems to arise from the same combo being
#   created from the dups.
# * TC should be at least 2^N because we are returning # of
#   combinations.

# IDEA
# ========
# Use backtracking such that for each index, we consider:
#   1) Including this number
#   2) Skipping it


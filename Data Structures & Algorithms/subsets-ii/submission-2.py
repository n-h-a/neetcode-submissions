class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res


# GOAL
# ========
# Given an array of ints (which may contain dups),
# return all possible subsets.

# OBSERVATIONS
# ========
# * Subsets, no dups => care about indices.
# * Actually creating subsets not counting, so DP trivial.

# IDEA
# ========
# Use backtracking: For each index, consider two possibilities:
#   1) Including that number
#   2) Not including that number
# Initialize two arrays for result and subset.
# Sort the array to help remove dups.
# Define a recursive function, dfs(i):
#   If we're considering past the last index (or last level):
#       Add a copy of the subset to result and return early.
#   Otherwise,
#       Add the number to subset and call dfs on next index with it.
#       Skip all dups.
#       Pop the number from subset and call dfs on next index w/o it.
# TC: O(N * 2^N)
# SC: O(N * 2^N)
# Why do we need to skip dups?
#   We skip dups because dfs on the first occurrence of an element
#   produces the same path/subsets as the dups. You can think of the
#   branches as (subsets including this element VS subsets that don't at all).

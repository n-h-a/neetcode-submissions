class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
                
# GOAL
# =========
# Given an array of unique ints, return all
# possible subsets of nums.

# BRUTE FORCE
# =========
# Start with one subset: the empty set.
# For every number in the array, 
#   Take all subsets so far and create new ones by adding
#   the current number to each of them.
# TC: O(N * 2^N)
# SC: O(N)

# IDEA
# =========
# Use backtracking: For each index, we want to
# consider two possibilities:
#       1) Including the number
#       2) Not including the number
# Initialize a result and an array to hold
# the subset we're building.
# Define a recursive function dfs(i):
#   If we're past considering the last index,
#       Add a copy of subset to result.
#       Return.
#   Otherwise,
#       Add the number to subset.
#       Consider dfs on next index with it.
#       
#       Remove the number from subset.
#       Consider dfs on next index without it.
# Call dfs on 0 and return result.
# TC: O(N * 2^N)
# SC: O(N)
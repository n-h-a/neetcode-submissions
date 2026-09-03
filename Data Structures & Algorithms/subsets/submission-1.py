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

[1, 2, 3]

[1]


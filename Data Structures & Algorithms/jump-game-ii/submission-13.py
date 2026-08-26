class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
            
        def dfs(i):
            if i == len(nums) - 1:
                return 0

            if i in memo:
                return memo[i]
            
            end = min(len(nums) - 1, i + nums[i])
            best = float('inf')

            for j in range(i + 1, end + 1):
                best = min(best, 1 + dfs(j))

            memo[i] = best
            return best

        return dfs(0)
        
        
# GOAL
# =======
# Given an array of jump lengths, return the min
# number of jumps needed to reach the last position
# in the array.

# BRUTE FORCE
# =======
# Use recursion with memoization.
# Define dfs(i):
#   If we're at the end, we do no jumps so 0.
#   If we've already done this work, return memo[i].
#   Otherwise,
#       Keep track of the best, min jump option.
#       Try out dfs on index j from [i + 1, i + jump at i].
#       Update memo for i and return best, min jump option.
# TC: O(N^2)
# SC: O(N)
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
# Use recursion.
# Define dfs(i, jumps):
#   If we're at the end, update res compared to jumps.
#   Otherwise,
#       Try out index j in range from i + 1 to i + jump at i.
#           dfs(j, jumps + 1)
# TC: O(N!)
# SC: O(N)
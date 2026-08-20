class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N <= 1:
            return 0

        pre_max = [0] * N
        post_max = [0] * N

        for i in range(1, N):
            pre_max[i] = max(height[i - 1], pre_max[i - 1])

        for i in range(N - 2, -1, -1):
            post_max[i] = max(height[i + 1], post_max[i + 1])
        
        res = 0
        for i in range(1, N - 1):
            water = min(pre_max[i], post_max[i]) - height[i]
            res += max(0, water)
        return res


# GOAL
# ==========
# Return max area of water that can be trapped
# between bars.

# NOTES
# ==========
# * array can be len 1

# OBSERVATIONS
# ==========
# Water can be above bars
# Edges don't count, must be between bars
# It's all about finding the max heights before and after.

# BRUTE FORCE
# ==========
# For each index,
#   Find tallest left height
#   Find tallest right height
#   Calculate amount of water that can be there.
#       min(leftMax, rightMax) - height[i]
# TC: O(N^2)
# SC: O(1)
# ISSUE: Redoing the process of finding
# tallest left height and right height
# over and over again.

# IDEA
# ==========
# Precompute prefix max on left and postfix max on right.
# For each index, calculate amount of water that can
# be above it.
# TC: O(N)
# SC: O(N)



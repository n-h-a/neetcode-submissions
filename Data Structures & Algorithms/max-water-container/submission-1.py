class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            
            while l + 1 < r - 1 and heights[l + 1] == heights[r - 1]:
                l += 1
                r -= 1
                area = min(heights[l], heights[r]) * (r - l)
                max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

        

# GOAL
# =========
# Return maximum amount of water a container can store.

# OBSERVATIONS
# =========
# Answer is not necessarily max height of both ends.
# When do we move the pointers?
#   Compare one after left to one before right. Take biggest.
#       Check: Does that yield the most optimal result at every given step?
#       Check: What if they're the same height?
#           Repeat process.

# IDEA
# =========
# Use two pointers. One at both ends.
# While left <= right,
#   Calculate area.
#   Update max if needed.
#   
#   While one after left != one before right,
#       Increment left
#       Decrement right
#   Take biggest.
#   
# Return max.
# TC: O(N)
# SC: O(1)
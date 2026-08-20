class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        
        max_area = 0

        while l < r:
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
#   GOAL: Eliminate pointer that cannot lead to better answer.
#   CLAIM: Keeping pointer at smaller line never yields a better answer.
#       PROOF: 
#           Width gets smaller as other pointer moves inward,
#           but height is at most whatever pointer at og smaller line is.
# 
#           SHOW: area of containers w/ that condition < area of o.g. container
#           area = width smaller * height at most L
#           og area = og width * height L
# 
#           Thus, keeping pointer at smaller line never yields a better answer
#           b/c every container w/ that condition will always be less
#           than the one we just checked.
# What if the pointers point to lines with the same height?
#   CLAIM: Either choice will yield the same possibilities.
#       PROOF: 
#           From previous claim, if every container made with smallest line
#           is no bigger than the one we checked, this should hold for both pointers.

# IDEA
# =========
# Use two pointers. One at both ends.
# While left <= right,
#   Calculate area.
#   Update max if needed.
#   if height[l] < height[r]:
#       Increment left
#   else:
#       Decrement right
# Return max.
# TC: O(N)
# SC: O(1)
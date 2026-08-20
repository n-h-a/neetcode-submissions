class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
    
# GOAL
# =========
# Return the area of the largest rectangle that can be formed 
# among the bars.

# BRUTE FORCE
# =========
# While there is still a num > 0 -- O(max value),
#   Subtract one from each num -- O(N).
#   Loop through nums again and count largest sequence
#   of non-zero nums -- O(N).
# TC: O(max val * N)

# IDEA
# =========
# Where is brute force suboptimal?
#   It loops through heights we already know don't contribute to the max.
#   When its just the max height left, we know the max count it can give is 1.
# Consider three cases of two heights:
# 1) first < second 
#       The first AND second can extend
# 2) first == second
#       The first AND second can extend
# 3) first > second
#       ONLY the second can extend
# Takeaway: Every height we care about is going to be increasing order.
#   We get rid of the ones that aren't in increasing order.

# PSEUDOCODE
# =========
# For every index, i, and height, h,
#   Save i as the start.
#   While stack is not empty and top of stack is taller than h,
#       Pop top of stack for index, idx, and height.
#       Calculate max area that could've been given by
#           top of stack.
#       Set start to idx to extend it backwards since we know
#       that the one we just popped was > current height.
#   Add start and current height to stack.
# For every remaining height in stack, calculate possible 
# max areas that extend all the way to the end.
# TC: O(N)
# SC: O(N)
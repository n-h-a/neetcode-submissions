class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_val = max(heights)
        max_count = 0

        for i in range(max_val):
            count = 0

            for j in range(len(heights)):
                if heights[j] > 0:
                    count += 1 * (1 + i)
                    max_count = max(max_count, count)
                    heights[j] -= 1
                else:
                    count = 0

        return max_count



# *   * 
# *   * 
# *   * 
# *   *     *
# *   *     *
# *   * * * *
# * * * * * *

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




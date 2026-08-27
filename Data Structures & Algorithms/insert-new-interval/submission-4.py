class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res
        

# GOAL
# ========
# Given an array of sorted, non-overlapping intervals and a new interval,
# return the array with new interval inserted. Maintain the sorted and
# non-overlapping properties by merging if necessary.

# BRUTE FORCE
# ========
# Linear Pass
# Skip past all the ones that end before new interval starts.
# If new interval overlaps, merge it.
#   i.e., intervals that start before new interval ends.
# Add all intervals that start after new interval ends.
# TC: O(N), SC: O(N)
# 
# Binary Search
# Use binary search to find where new interval should go.
# Insert it, then do a linear pass to merge overlapping.
# TC: O(N), SC: O(N)

# IDEA
# =========
# Case by Case: Each interval is either:
# 1. Completely after newInterval
#       Insert new interval and return the res appended.
# 2. Completely before newInterval
#       Insert current interval.
# 3. Overlapping with newInterval
#       Merge interval
# TC: O(N), SC: O(N)
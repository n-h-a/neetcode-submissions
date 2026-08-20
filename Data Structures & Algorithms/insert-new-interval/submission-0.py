class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res


# GOAL
# =======
# Given an array of non-overlapping sorted intervals and a new 
# interval, return the array with the new interval inserted. 
# Preserve the non-overlapping and sorted properties.

# OBSERVATIONS
# =======
# What matters is the starts.
# If there's an overlap, then we merge.

# BRUTE FORCE
# =======
# Add intervals completely before new interval.
# Handle intervals that overlap with new interval.
# Add intervals completely after merged new interval.
# TC: O(N)


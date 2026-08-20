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
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
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

# IDEA
# =======
# Binary Search
#   * Use binary search to find the pos where newInterval should
#     be sorted based on start time.
#   * Loop through list and merge intervals.
#   TC: O(N)
# Greedy
#   * Completely after newInterval
#       If new interval ends before current, then place newInterval
#       there and return answer.
#   * Completely before newInterval
#       If current interval ends before new, then add to res
#       unchaned.
#   * Overlapping with newInterval
#       If they overlap, merge.
#   TC: O(N)
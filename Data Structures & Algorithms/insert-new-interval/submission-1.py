class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
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


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else: 
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res

# GOAL
# ========
# Given an array of intervals, return the minimum num of intervals
# needed to be removed to have non-overlapping intervals.

# BRUTE FORCE
# ========
# Use recursion.
# Sort the intervals by start time.
# For each interval, 
#   Base case: If interval at end, return 0.
#   Consider possibility where we don't include it.
#   Consider possibility where we do include it, but ensure it
#       doesn't overlap.
#   Take the max of both possibilities and return. 
# TC: O(2^N)
# SC: O(N)
# 
# Use top down DP.
# Initialize a memo.
# Sort the intervals by end time.
# Perform dfs(i) starting from index 0:
#   If i in memo, return stored result, memo[i].
#   Start res at 1 (to count the current interval).
#   For every index j after,
#       res = max(res, 1 + dfs on j).
#   Store res in memo.
#   Return res.
# Return length of intervals - max # of intervals.
# TC: O(N^2)
# SC: O(N)
# 
# Use bottom up DP.
# Initialize a memo.
# Sort the intervals by end time.
# For each interval,
#   Start at dp[i] = 1.
#   For every interval at j before i,
#       If interval[j] doesn't overlap with interval[i],
#           Set dp to the max of
#               * the best dp[i] found so far
#               * # of intervals if interval[i] placed after interval[j]
#       Find the max # of intervals from dp.
# Return length of intervals - max # of intervals.
# TC: O(N^2)
# SC: O(N)
# 
# Use DP with binary search.
# Sort the intervals by end time.
# For each interval,
#   Find pos of latest interval that doesn't overlap with current.
#   If no such pos / interval exists, just set dp[i] to dp[i - 1].
#   Otherwise,
#       Set dp[i] to the max of either skipping interval or taking it.
# Return length of intervals - max # of intervals.
# TC: O(N log N)
# SC: O(N)

# IDEA
# ========
# Use greedy algorithm.
# Sort the intervals by start time.
# Initialize res = 0 and prevEnd to end of first interval.
# For each interval (start, end),
#   If start >= prevEnd, there is no overlap. Update prevEnd to end.
#   Otherwise, there is an overlap and we need to remove one.
#       Increment res.
#       Keep interval with smaller end by setting prevEnd = min(end, prevEnd).
# Return res.
# TC: O(N)
# SC: O(1)




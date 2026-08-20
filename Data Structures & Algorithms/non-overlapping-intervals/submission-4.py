class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        n = len(intervals)
        dp = [0] * n
        dp[0] = 1

        def bs(r, target):
            l = 0
            while l < r:
                m = (l + r) >> 1
                if intervals[m][1] <= target:
                    l = m + 1
                else:
                    r = m
            return l

        for i in range(1, n):
            # Find idx, the first pos in [0, i) s.t. intervals[i] doesn't overlap.
            idx = bs(i, intervals[i][0])

            # If no such interval exists, take intervals[i] alone. Compare with skipping.
            if idx == 0:
                dp[i] = dp[i - 1]
            else:
                # Otherwise, skip interval i or take it.
                dp[i] = max(dp[i - 1], 1 + dp[idx - 1])
        
        return n - dp[n - 1]

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





class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            # Push valid intervals onto min heap.
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # Pop invalid intervals off of min heap.
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Retrieve smallest valid length.
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

# GOAL
# ======
# Given a list of intervals and a list of time queries, return
# the length of the shortest interval for each time query.

# BRUTE FORCE
# ======
# Create dictionary to map moment in time -> min interval.
# For each time,
#   Loop through list of intervals.
#   Update mapping to hold min interval it exists in.
# TC: O(10^7 * N)
# SC: O(10^7)
# Small optimization: Find max end time first.

# IDEA
# ======
# Sort intervals and queries and use min heap to
# store min length and ends.
# For every query (in sorted order),
#   Add candidate intervals to the min heap.
#       Intervals are candidates iff the start of
#       the interval < query time. Push onto
#       heap as (interval length, end).
#   Remove invalid candidate intervals.
#       Intervals are invalid if their ends
#       are < query time. Pop from the heap.
#   Retrieve smallest valid interval from top of
#   min heap if exists and store in dictionary.
# Build output list from dictionary and return.
# TC: O(N log N + Q log Q)
# SC: O(N + Q)


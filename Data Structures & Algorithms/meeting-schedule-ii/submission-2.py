"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda i: i.start)
        
        max_size = 1
        min_heap = [intervals[0].end]
        heapq.heapify(min_heap)

        for i in range(1, len(intervals)):
            if min_heap[0] <= intervals[i].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i].end)
        return len(min_heap)

# GOAL
# ========
# Given an array of intervals, return the min # of batches
# required to schedule all intervals w/o overlaps.

# BRUTE FORCE
# =======
# Use greedy algorithm.
# Sort the intervals by end time.
# Place the first interval in the first batch.
# For each interval,
#   Added = False
#   For each batch, 
#       Check if it doesn't overlap with the last element.
#           If beginning of current >= end of last,
#               Append it to batch.
#               Added = True
#   If not Added, create a new batch.
# Return the # of batches.
# TC: O(N^2)
# SC: O(N)
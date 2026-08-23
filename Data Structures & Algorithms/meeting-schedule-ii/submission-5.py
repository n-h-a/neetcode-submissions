"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)
        return res
# GOAL
# ========
# Given an array of intervals, return the min # of batches
# required to schedule all intervals w/o overlaps.

# BRUTE FORCE
# =======
# Use batches.
# Sort the intervals by start time.
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
# Not optimal because we have to look through the batches.
# 
# Use min heap to keep track of earliest end time.
# Sort the intervals by start time.
# For each interval,
#   Check if it is >= than earliest end time.
#       If yes, then we can reuse that room, so we pop and push the new end time.
#       Otherwise, we can't reuse that room, and therefore every other room is
#           busy because it's the earliest end time. We push a new end time to
#           represent a new room.
# Return the length of the min_heap.
# TC: O(N log N)
# SC: O(N)


# IDEA
# =========
# We want to know the max # of meeting rooms at any given time.
# Sort start times.
# Sort end times.
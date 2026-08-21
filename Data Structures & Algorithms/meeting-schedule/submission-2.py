"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True

# GOAL
# =======
# Given an array of intervals, return true if there are
# no overlaps. Otherwise, return false.

# IDEA
# =======
# Sort intervals by start time.
# For each interval,
#   Check if there is an overlap. Return false if yes.
# Return True.
# TC: O(N log N)
# SC: O(N)
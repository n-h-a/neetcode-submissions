class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intrvls = sorted(intervals, key=lambda intrvl: intrvl[0])
        print(intrvls)

        if len(intrvls) <= 1:
            return intrvls

        res = []
        new = intrvls[0]
        for i in range(1, len(intrvls)):
            curr = intrvls[i]
            if new[1] >= curr[0]:
                new = [
                    new[0],
                    max(new[1], curr[1])
                ]
            else:
                res.append(new)
                new = curr
        res.append(new)
        return res

# GOAL
# ========
# Given an array of intervals, return an array of
# non-overlapping intervals by merging overlapping ones.

# OBSERVATIONS
# ========
# In sorted, overlapping means:
#   First of second <= End of first

# BRUTE FORCE
# ========
# Sort all intervals by start time.
# Keep a variable to build an interval to add to res, new.
# Loop through the intervals,
#   If new overlaps with interval we're currently looking at,
#       Update new.
#   Otherwise,
#       new is good to add to res. Add it to res then update to curr.
# TC: O(N log N)
# SC: O(N)
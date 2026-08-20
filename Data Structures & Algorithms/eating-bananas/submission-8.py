class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            rate = lo + (hi - lo) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / rate)
            if hour <= h:
                hi = rate - 1
            else:
                lo = rate + 1
        return lo

# GOAL
# ========
# Return min k s.t. I can eat all bananas within h hours.

# NOTES
# ========
# * Each hour, choose any pile and eat k.
# * If pile < k, can eat all, but not from another within the hour.
#       EX: [1, 1], h = 1
#           If k == 2, hour 1: pile[0]
#                      hour 2: pile[1]
#           Cannot eat both piles in hour 1.
# * One pile per hour.

# OBSERVATIONS
# ========
# * If h is always at least the length of piles,
#   then the max possible rate is the max value in piles.
#       For each pile, we could just eat the max value.
#       Guarantee we will satisfy hour requirement b/c
#           min hour is length of piles.
# * Our search space [1, max value in piles], which is sorted.
# * How do we calculate # of hours per pile?
#       ceil(pile / rate)

# BRUTE FORCE
# ========
# For each potential rate [1, max pile value] -- O(M).
#   hour = 0
#   For each pile -- O(N).
#       hour += ceil(pile / potential rate)
#   If hour <= h,
#       return potential rate
# TC: O(M * N)
# SC: O(1)

# IDEA
# ========
# Why is brute force suboptimal?
#   We traverse every possible rate. This is O(M) s.t. M is the max value in the list.
#   Since the potential rates are sorted, we can look for it faster
#       using binary search.
# Conduct binary search on potential rates.

# PSEUDOCODE
# =========
# lo = 1
# hi = max(piles) -- O(N)
# while lo <= hi -- O(log M)
#   calculate mid, aka our potential rate
#   hour = 0
#   For each pile -- O(N).
#       hour += ceil(pile / potential rate)
#   If hour <= h,
#       that means the potential rate is valid but could be too high.
#       Move hi to mid - 1.
#   If hour > h,
#       that means the potential rate is invalid b/c it is too low.
#       Move lo to mid + 1.
# Return hi.
# TC: O(N log M)
# SC: O(1)
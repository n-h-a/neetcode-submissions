class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len = 0, 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            
            seen[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len
        

# GOAL
# =========
# Return the length of the longest substring without duplicates.

# BRUTE FORCE
# =========
# For each character,
#   Find the length of a substring without dups.
#   Update max.
# TC: O(N^2)

# OBSERVATIONS
# =========
# Have to traverse the entire string to consider all possibilities -> O(N)
# What makes the brute force solution suboptimal?
#   Sometimes, finding a substring without dups means
#   traversing a part of a substring that you already
#   traversed.

# IDEA
# =========
# GOAL: Avoid traversing already traversed non-dup strings.
#       Shrink window if dup found.
#       Extend window foward as long as there's no dups.
# Use two pointers - sliding window technique.
# l = 0, r = 1, max_len = 1
# seen = {s[0] : 0}
# While the r pointer does not go past the end,
#   if s[r] has been seen,
#       move l to max of itself or one past where s[r] was last seen
#   update found[s[r]] to r
#   update max
# Return max length
# TC: O(N)
# SC: O(M) s.t. M is # of unique letters

# If I encountered some duplicate, that means
# I need to move the l such that there are no more duplicates. 
# The duplicate could have appeared anywhere, meaning l
# should go after the index where the letter was first found.
# Or stay the same if that letter is before l.



 
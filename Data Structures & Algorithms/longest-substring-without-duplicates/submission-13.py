class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        l = 0
        seen = {}
        for r in range(len(s)):
            letter = s[r]
            while letter in seen and seen[letter] > 0:
                seen[s[l]] -= 1
                l += 1

            seen[letter] = 1
            max_len = max(max_len, r - l + 1)

        return max_len


# GOAL
# =========
# Return length of longest substring without dups.

# BRUTE FORCE
# =========
# For each letter,
#   Construct a substring while there is no dups.
#   Update max.
# TC: O(N^2)
# SC: O(1)
# Is there any extra work? Yes, we sometimes may go over 
# substrings we already checked for dups.

# IDEA
# =========
# Use sliding window approach.
# Shrink window from left until there are no dups.
# Expand window from right.

# PSEUDOCODE
# =========
# Initialize left pointer.
# For every letter in the string,
#   If there is a duplicate,
#       Shrink the window from the left
#   Record max


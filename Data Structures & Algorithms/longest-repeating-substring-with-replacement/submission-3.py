class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

# GOAL
# =========
# Return the length of the longest substring containing
# only one distinct char after performing <= k replacements.

# OBSERVATIONS
# =========
# We want to figure out how to make a substring only have
# one distinct char. However, we can only do <= k replacements.
#   There will be invalid 
#       [substrings with > one distinct char after <= k replacements]
#   and valid strings
#       [substrings with one distinct char after <= k replacements].
# How can we check if a string is valid?
#   The best way to make a substring into valid is to
#       change every other letter to the most frequent
#       letter. EX: AAABA -> Change B to A
#   Keep a frequency map to track max_freq.
#   Check if each substring is valid. Update max len.

# BRUTE FORCE
# =========
# For each substring - O(N^2),
#   Construct frequency map, keep track of max_freq.
#   If substring is valid [len(substring) - max_freq <= k]
#       Update length
# TC: O(N^3)
# SC: O(N)

# IDEA
# =========
# How is brute force suboptimal?
#   We're constructing a new frequency map for every substring.
#       But some substrings consist of the same frequency map minus a
#       few chars/counts.
#   We're checking bigger versions of substrings that are invalid.
#       Making an invalid substring bigger will not make it valid.
# Use sliding window for frequency map and to move on from
# invalid substrings.
#   Shrink when invalid until valid.

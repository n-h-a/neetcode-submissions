class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i

        res = []
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])

            if i == end:
                res.append(size)
                size = 0

        return res
        
# GOAL
# =======
# Given a string s, we want to split the string into
# as many substrings as possible, while ensuring that
# each letter appears in at most one substring. Return
# a list of ints representing the size of these ints
# in order.

# OBSERVATIONS
# ========
# * For each letter, we care about the first and last occurrence,
#   which create a range.
# * If there are overlaps in the ranges, they belong to the same
#   string.

# IDEA
# ========
# Loop through list to keep track of last occurrences.
# Use a variable to keep track of string length.
# For each letter in the string,
#   Increment current partition size.
#   Update end if needed.
#   If current position == end, add to result and reset size.
# Return result.
# TC: O(N)
# SC: O(M) s.t. M is # of unique characters.
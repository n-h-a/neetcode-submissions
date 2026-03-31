class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# GOAL
# ========
# Given a list of strings,
#   Return a list of list of strings s.t. each sublist has anagrams.

# NOTES
# ========
# * Can have empty strings
# * strs length at least 1

# BRUTE FORCE
# ========
# For each string in strs,
#   For every other string in strs,
#       Check if characters match.

# IDEA
# ========
# Result is a dictionary that maps a frequency tuple to a list of strings.
# For each string in strs,
#   Create a frequency list and fill it in.
#   Convert frequency list to a tuple and add entry to result.



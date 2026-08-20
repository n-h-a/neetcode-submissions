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
# =======
# Group all anagrams together.
# Output: List of list of strings.

# OBSERVATIONS
# =======
# Need to loop through complete list, and entire strings.

# PSEUDOCODE
# =======
# IDEA: Use dictionary s.t. key == frequency list and value == strings.
# Loop through strs,
#   Create a frequency list.
#   Use the frequency list as a key in res, and append s.
#   NOTE: Need to convert list to tuple b/c keys have to be immutable.
# TC: 
#   len(strs) == N
#   max len of string = M
#   => O(N * M)
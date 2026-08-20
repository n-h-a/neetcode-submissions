class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = set()
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in sorted_strs:
                    res[sorted_s].append(s)
            else:
                sorted_strs.add(sorted_s)
                res[sorted_s] = [s] 

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
# Keep a set of sorted strings.
# Loop through strs,
#   Sort current string.
#   If string exists in set, add to result.
#   Otherwise, add into set and create new entry in result.
# TC: 
#   len(strs) == N
#   max len of string = M
#   => O(N * M log M)
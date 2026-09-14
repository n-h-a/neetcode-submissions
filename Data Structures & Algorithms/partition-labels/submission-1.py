class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for i in range(len(s)):
            last_idx[s[i]] = i

        res = []
        smallest, furthest = 0, 0
        for i in range(len(s)):
            furthest = max(furthest, last_idx[s[i]])

            if i == furthest:
                res.append(furthest + 1 - smallest)
                smallest = furthest + 1
                continue
        
        return res


            
        

# GOAL
# ======
# Given a string, return a list of substring sizes
# s.t. no letters appear in more than one substring.


# OBSERVATIONS
# ======
# * For each letter, we care about its latest occurence.

# BRUTE FORCE
# ======
# For each letter, create a list of intervals.
# Merge overlapping intervals. Return sizes.

# IDEA
# ======
# Use two pointer greedy approach.
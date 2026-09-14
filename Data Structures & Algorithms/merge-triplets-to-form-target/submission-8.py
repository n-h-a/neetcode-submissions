class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        curr = []
        for candidate in triplets:
            cand_x, cand_y, cand_z = candidate

            if cand_x > x or cand_y > y or cand_z > z:
                continue
            
            if not curr:
                curr = candidate
            else:
                curr = [
                    max(cand_x, curr[0]), 
                    max(cand_y, curr[1]), 
                    max(cand_z, curr[2])
                ]
            
            if curr == target:
                return True
        print(curr)
        return False
            
        
# GOAL
# =======
# Given an array of triplets and a target triplet,
# return True if it is possible to obtain the target
# by applying zero or more "max operations".

# OBSERVATIONS
# =======
# * Any triplet with an ith element > target's ith element
#   should not be considered.
# * We can max perform max operations on all the rest,
#   and if any of them == target, return True. Otherwise, False.


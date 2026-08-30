class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        targ_x, targ_y, targ_z = target

        candidate = []
        for i in range(len(triplets)):
            x = triplets[i][0]
            y = triplets[i][1]
            z = triplets[i][2]

            if x > targ_x or y > targ_y or z > targ_z:
                continue

            if not candidate:
                candidate = triplets[i]
            else:
                candidate = [
                    max(candidate[0], x),
                    max(candidate[1], y),
                    max(candidate[2], z)
                ]

        if candidate == target:
            return True
        return False

# GOAL
# ========
# Given an array of triplets and a target triplet,
# retrun true if it is possible to obtain the target
# through the following operation 0 or more times:
#   Update a triplet to be the max of each of its elements
#   compared to another triplet's corresponding elements.

# OBSERVATION
# ========
# * The only triplets that can yield the target through
#   this operation satisfy the following:
#       All elements are <= target's corresponding elements.
# * Every other triplet can be used in comparison to reach
#   the target triplet.
# * If any of the comparison triplets make an element >
#   the corresponding target element, it's invalid.

# IDEA
# =======
# For each triplet,
#   If any elements are > target's corresponding,
#       Skip past it.
#   Otherwise, apply the operation.
#       If it equals target, return true.
#       Otherwise, continue.
# Return false.

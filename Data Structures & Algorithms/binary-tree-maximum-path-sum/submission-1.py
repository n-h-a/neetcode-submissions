# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def recurse(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_max = max(0, recurse(node.left))
            right_max = max(0, recurse(node.right))

            joint = node.val + left_max + right_max
            cut_left = node.val + left_max
            cut_right = node.val + right_max

            max_sum = max(max_sum, joint, cut_left, cut_right)

            return max(cut_left, cut_right)

        recurse(root)
        return max_sum


# BRUTE FORCE
# =========
# Generate all possible paths --> O(N^2),
# Compute sum for each. Update max. 
# TC: O(N^3)

# Observations
# =========
# For each node, we consider:
#   1) Path constructed if the node is a "joint".
#   2) Path constructed if the node pics only one side.
# For both options:
#   We want the max from the left + max from the
#   right such that there are no "joint" sums.

# IDEA
# =========
# Observations:
#   1. Cannot have more than two joints in one sum.
# For each node,
#   We consider two options:
#       1) Joint: The sum of a path constructed from the left & right side.
#       2) Cut: The sum of a path constructed by choosing one side.
#   We update max in both cases, but we return only the max cut up.
# TC: O(N)
# SC: O(N)
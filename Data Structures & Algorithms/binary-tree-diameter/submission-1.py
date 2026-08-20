# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        self.diameter = max(
            self.diameter,
            left_height + right_height
        )
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

# GOAL
# =======
# Given the root of a binary tree,
# return the diameter of a tree.

# NOTES
# ======
# Diameter is the max number of edges between
# two nodes.

# BRUTE FORCE
# ======
# For each node, calculate the length of the path 
# between it and another. Update max length as you go.
# TC: O(N^2) s.t. N is the number of nodes.

# IDEA
# ======
# Why is brute force suboptimal?
#   We are traversing the same edges. Some paths
#   include other paths and we iterate through them
#   again.
# Is there a way we could do one pass between the nodes?
#   Observations
#       * Edges in a path vary by levels, so depth matters.
#       * The root might not be in the longest path (diameter).
#       * If it was though, the diameter would be
#           the path to the deepest node on the right +
#           the path to the deepest node on the left
#       * Deepest node == height of tree.
#   For each node,
#       We add the height of the left tree + the height of the right tree.
#       Update max.
# TC: O(N)
# SC: O(log N) if balanced, O(N) if not.
      




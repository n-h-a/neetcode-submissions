# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Save the original nodes.
        og_left = root.left
        og_right = root.right

        # Switch the nodes and perform the process on their children.
        root.left = self.invertTree(og_right)
        root.right = self.invertTree(og_left)

        return root

# GOAL
# =======
# Given the root of a binary tree,
# invert the tree and return its root.

# OBSERVATIONS
# =======
# Inversion: For each node, each child is switched around

# IDEA
# =======
# B/c inversion is just the children switched around
# for each node, we can perform recursion.
# TC: O(N) s.t. N is the # of nodes.
# SC: O(N)
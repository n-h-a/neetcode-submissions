# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if max(p.val, q.val) < curr.val:
                curr = curr.left
            elif min(p.val, q.val) > curr.val:
                curr = curr.right
            else:
                return curr

# GOAL
# =======
# Given a BST and two nodes p and q from it,
# return their least common ancestor (LCA).

# IDEA
# =======
# For each node,
#   If p and q are smaller, 
#       Search the left subtree.
#   If p and q are bigger,
#       Search the right subtree.
#   Else (at least one is equal to current OR one is bigger and one is smaller),
#       The node is a split point.

# TC: O(h)
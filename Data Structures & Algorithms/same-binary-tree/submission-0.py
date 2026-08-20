# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes DNE, return True
        if not p and not q:
            return True

        # If only one node exists, return False
        if (p and not q) or (q and not p):
            return False

        same_value = p.val == q.val
        left_equiv = self.isSameTree(p.left, q.left)
        right_equiv = self.isSameTree(p.right, q.right)
   
        return same_value and left_equiv and right_equiv

# GOAL
# =======
# Given two binary trees, return true if they are
# equivalent. False otherwise.

# IDEA
# =======
# Equivalent means they share:
#   1) the exact same strucutre
#   2) the exact same values
# For each subtree,
#   Root needs to be the same
#   Right needs to be the same
#   Left needs to be the same

# PSEUDOCODE
# =======
# If the roots are not the same, return False.
# If the left subtrees are not the same, return False.
# If the right subtrees are not the same, return False.
# Otherwise, return True.
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and q and p.val == q.val:
            return (self.sameTree(p.left, q.left) and
                    self.sameTree(p.right, q.right))
        return False

# GOAL
# =======
# Given two roots, subroot and root, return True
# if there exists a subtree of root s.t. it is the
# exact same as the tree of subroot.

# BRUTE FORCE
# =======
# For each root,
#   Check if it is the same as the subroot tree:
#       Check if roots are same.
#           Check if left subtrees are same.
#               Check if right subtrees are same.
# TC: O(M * N)
# SC: O(M + N)

# IDEA
# =======
# Why is brute force suboptimal?
#   We're traversing the same nodes repeatedly.
#   Is there a way we could do one pass?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return (
                dfs(node.left, left, node.val) and
                dfs(node.right, node.val, right)
            )
        return dfs(root, float("-inf"), float("inf"))

# GOAL
# ========
# Given a binary tree, return true
# if it is a BST.

# IDEA
# ========
# Definition of BST:
#   Everything to the left of the root is <
#   Everything to the right of the root >
#   Left amd right subtrees are BSTs
# Observation
#   Each root is...
#       The max of the left subtree
#       The min of the right subtree
#   Each root is limited by a range according to their ancestors.
#       For example, 2 is limited by [1, 4]. 0 is limited by [-1, 1].
#                       4
#                   1       5
#               -1     2  
#           -2     0      3
# Perform DFS passing down the range.
# TC: O(N)
# SC: O(N)





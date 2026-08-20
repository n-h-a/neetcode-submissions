# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return (0, True)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
        return (1 + max(left[0], right[0]), balanced)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.dfs(root)[1]
        

# GOAL
# =======
# Given a binary tree, return tree if it is height balanced.
# Otherwise, return false.

# OBSERVATIONS
# =======
# * Height balanced: the left and right subtrees of ever
#   node differ in height by no more than 1.
# Edge case:
#   If the tree is empty, return true.

# IDEA
# =======
# Given this definition, we can recursively check if
#   the height of the left and right subtrees differ by 1 for
#   each node.
# TC: O(N^2)
# SC: O(N
# 
# There's two things we need to do:
#   1) Track the height
#   2) Compare the height of the two subtrees.
#       If the difference > 1, return false.
#       Otherwise, return true.
# We do a recursive approach where we return two things:
#   1) the height
#   2) whether the tree is balanced at that point

# PSEUDOCODE
# =======
# For each node,
#   If DNE, return [0, True].
#   
#   Call DFS on left.
#   Call DFS on right.
# 
#   Return 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# GOAL
# =======
# Given the root of a binary tree, return its depth.

# OBSERVATIONS
# =======
# Depth could be defined as the # of levels (BFS)
#   or as the # of nodes along the longest branch (DFS).

# IDEA
# =======
# Use BFS to do this.
# Every time I move down a level, I add to depth.
#   How do I know when I moved down a level?
#       I can calculate the number of children added at each round.
#       Process the queue up until that point.
# TC: O(N) s.t. N is the number of nodes
# SC: O(N)
# 
# Use DFS to do this.
# The depth of any tree is just 1 + max depth found between the right and left subtrees.
# TC: O(N) s.t. N is the number of nodes.
# SC: O(log N) if tree balanced.
#     O(N) if unbalanced.
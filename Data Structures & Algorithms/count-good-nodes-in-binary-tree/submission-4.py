# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            res = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            res += dfs(node.left, max_so_far)
            res += dfs(node.right, max_so_far)

            return res

        return dfs(root, root.val)

        
# GOAL
# =======
# Given a binary tree, return the # of good nodes (i.e.,
# their path to the root doesn't contain a value > them).

# OBSERVATIONS
# =======
# Root is included as a good node.

# BRUTE FORCE
# =======
# For each node,
#   Evaluate the path between it and the root.
#   Add to result if it is a good node.
# TC: O(N^2)

# IDEA
# =======
# Why is brute force suboptimal?
#   It goes down the same branch for each node.
# Perform DFS.
#   Keep track of the max found.
#   If current node is >= max, add it to the list.
#   Otherwise, continue.
# TC: O(N)
# SC: O(N)
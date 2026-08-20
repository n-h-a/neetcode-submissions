# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root



# OBSERVATIONS
# =========
# 1. First node of preorder is guaranteed to be the root of the tree.
# 2. The index of the root in inorder partitions inorder into the left and right subtrees.

# IDEA
# =========
# We can recursively:
# 1. Take the root from preorder.
# 2. Build the left and right subtrees by partitioning inorder at the root.
# TC: O(N^2)
# SC: O(N)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def inOrder(node):
            nonlocal count, answer

            if not node:
                return

            inOrder(node.left)

            count += 1
            if count == k:
                answer = node.val
                return
            
            inOrder(node.right)
        inOrder(root)
        return answer
        
# IDEA
# =======
# Traverse the BST in order (i.e., left, root, right).
# EXAMPLE:
#               4
#           2      5
#       1      3
# 
#   1 -> 2 -> 3 -> 4 -> 5
# For each root,
#   We add the left subtree count + 1.
#   If the result == k, return the result.
#   Otherwise, we return the result + the right subtree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            sublist = []
            for i in range(level_size):
                curr = queue.popleft()
                if curr:
                    sublist.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if sublist:
                result.append(sublist)
        return result

# GOAL
# ========
# Given a binary tree, return the level
# order traversal of it as a nested list.

# IDEA
# ========
# We can traverse the tree using BFS and a queue:
#   Initialize result.
#   Initialize queue to the first node.
#   While queue not empty,
#       Get the length of the queue.
#       Initialize a sublist.
#       Until we reach the length,
#           Get the current node.
#           Add their children into the sublist.
#       Append the sublist to result.
#   Return result.
# TC: O(N)
# SC: O(N)
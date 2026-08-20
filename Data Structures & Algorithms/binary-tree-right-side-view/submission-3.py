# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            q_size = len(queue)

            for i in range(q_size):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
                if i == q_size - 1:
                    res.append(curr.val)
        return res

# GOAL
# =======
# Given a binary tree, return the values of the nodes
# visible from the right, ordered from top to bottom.

# OBSERVATIONS
# =======
# The nodes visible from the right are the
# ones at the end of each level.

# IDEA
# =======
# Perform BFS and only add the last node of each level to the result.
#   Initialize a result and queue.
#   Add node to the queue.
#   While the queue is not empty,
#       Get the length of the queue.
#       Until we reach the length of the queue,
#           Get the current node.
#           If left and/or right children exist,
#               Add its children to the queue.
#           If the current node is the last in the level, 
#               add it to the result.
#  Return the result.
# TC: O(N)
# SC: O(N)
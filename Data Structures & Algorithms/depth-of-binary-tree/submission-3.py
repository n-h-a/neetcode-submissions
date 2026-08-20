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

        depth = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth

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
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(oldNode):
            if not oldNode:
                return None

            newNode = Node(oldNode.val)
            visited[newNode.val] = newNode

            newNeighbors = []
            for neighbor in oldNode.neighbors:
                if neighbor.val in visited:
                    newNeighbors.append(visited[neighbor.val])
                else:
                    newNeighbors.append(dfs(neighbor))

            newNode.neighbors = newNeighbors

            return newNode

        return dfs(node)
# IDEA
# =======
# Use DFS to traverse this graph since we need the neighbors to be created first.






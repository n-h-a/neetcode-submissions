"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def dfs(oldNode):
            if not oldNode:
                return None

            newNode = Node(oldNode.val)
            clones[oldNode] = newNode
            
            for neighbor in oldNode.neighbors:
                if neighbor in clones:
                    newNode.neighbors.append(clones[neighbor])
                else:
                    newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)

# IDEA
# =======
# Use BFS to traverse this graph.






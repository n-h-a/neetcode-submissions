"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {}
        idx, node = 0, head
        while node:
            mapping[node] = idx
            idx += 1
            node = node.next
        size = len(mapping)

        node = head
        nodes = [Node(0) for i in range(size)]
        for i in range(size):
            nodes[i].val = node.val
            nodes[i].next = None if i == size - 1 else nodes[i + 1]
            nodes[i].random = None if not node.random else nodes[mapping[node.random]]
            node = node.next

        return nodes[0]

# GOAL
# =========
# Given the head of a linked list with random pointers, 
# return a deep copy of the list.

# BRUTE FORCE 
# =========
# Create an hashmap for node-index mappings -- O(N).
# Create a list to store the new nodes.
# For each node -- O(N)
#   Update value of new to value of og.
#   Update value of next to next element of list.
#   Update value of random to node at og random's index. Use hashmap to get index.
# Return head.
# TC: O(2N) -> O(N)
# SC: O(2N) -> O(N)
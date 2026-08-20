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

        mapping = defaultdict(lambda: Node(0))
        mapping[None] = None

        node = head
        while node:
            mapping[node].val = node.val
            mapping[node].next = mapping[node.next]
            mapping[node].random = mapping[node.random]
            node = node.next

        return mapping[head]

# GOAL
# =========
# Given the head of a linked list with random pointers, 
# return a deep copy of the list.

# BRUTE FORCE 
# =========
# Create an hashmap s.t. the default value is a node.
# For each og node -- O(N)
#   Update its copy val to og val.
#   Update its copy next to the mapping of the og next (if DNE, default creates it).
#   Update its copy random to mapping of og random (if DNE, default creates it).
# Return copy of head.
# TC: O(N)
# SC: O(N)
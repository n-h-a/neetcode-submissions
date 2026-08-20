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

        return None if not nodes else nodes[0]

        


        


        


# GOAL
# =========
# Given the head of a linked list with random pointers, 
# return a deep copy of the list.

# BRUTE FORCE 
# =========
# Create an array.
# For each node in the o.g. list,
#   Create a new node with the value and next pointer.
#   Append it to the array.
# After creating the list,
#   You can start assigning the random pointer:
# For each node in the o.g. list, assign the random pointer.
 
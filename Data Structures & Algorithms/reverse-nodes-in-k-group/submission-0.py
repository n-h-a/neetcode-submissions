# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a list of nodes.
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        # Reverse every complete group of k.
        for end in range(k - 1, len(nodes), k):
            start = end - k + 1
            
            # Reverse pointers inside this group.
            for j in range(end, start, -1):
                nodes[j].next = nodes[j - 1]

            next_start = end + 1
            
            if next_start >= len(nodes):
                # Nothing comes after this group.
                nodes[start].next = None
            elif next_start + k - 1 < len(nodes):
                # If a group still exists, connect to the head of the next reversed group.
                nodes[start].next = nodes[next_start + k - 1]
            else:
                # If leftover nodes but no group, connect to leftover nodes that are not reversed.
                nodes[start].next = nodes[next_start]

        
        
        return nodes[k - 1]





# GOAL
# =======
# Given the head of a singly linked list and a
# positive int k, reverse the first k nodes, then
# the next, etc. Return the modified list.

# BRUTE FORCE
# =======
# Put the nodes in an array.
# For every group k,
#   Reverse the nodes.
# Return the modified list.
# TC: O(N)
# SC: O(N)

# OBSERVATIONS
# =======
# The beginning of first group points at the end of the next group.

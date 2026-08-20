# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 <- 1 <- 2 <- 3
#      *

# prev = 3
# current = null
# next = null
# current.next = 2

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        current = head.next
        prev.next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


# GOAL
# ========
# Given head of singly linked list, reverse the list +
# return the new beginning of the list.

# QUESTIONS
# ========
# Is the list sorted?
# Does the list just comprise of integers?

# BRUTE FORCE
# ========
# For every element of the list,
#   Create a new node and point to the head.
# TC: O(N)
# SC: O(N)

# IDEA
# ========
# Because we need to reverse the list, this requires
# going over every element. TC is at least O(N).
# How is brute force suboptimal?
#   We create new nodes for every element. Thus, 
#   SC is O(N). 
# Observations:
#   The reverse of a single element list is just the single element.
#   The reverse of an empty list is just the empty list.
# If the len(list) > 1, we save the previous node and the next node.
# Then, we have the current node point to the previous node.
# TC: O(N)
# SC: O(1)

# PSEUDOCODE
# ========
# If len(list) < 1:
#   Return the list as is.
# 
# Set prev node to first element in list.
# Set current node to second element in list.
# While current node doesn't point to null,
#   Save next node.
#   Set current node's next to prev node.
#   Set prev node to current node.
# Return current node.
# TC: O(N)
# SC: O(1)
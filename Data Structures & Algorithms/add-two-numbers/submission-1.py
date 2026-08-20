# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        
        carry = 0
        while l1 or l2:
            total = 0

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            total += carry
            carry = total // 10
            total %= 10

            tail.next = ListNode(total)
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)
        return res.next

# GOAL
# =======
# Given two non-empty linked lists that represent
# a non-negative integer stored in reverse order,
# return the sum of the two numbers as a linked list.

# QUESTIONS
# =======
# Is the list singly linked?

# IDEA
# =======
# Use two pointers.
# Have a carry variable.
# While l1 or l2 still has elements,
#   Keep a sum.
#   If l1 still has elements,
#       Add l1.val to sum.
#   If l2 still has elements,
#       Add l2.val to sum.
#   Add carry to the sum.
#   Set carry to sum // 10.
#   Set sum to sum % 10.
#   Add sum to result.
# If carry not 0, add new node.
# Return the head of sum.
# TC: O(N + M)
# SC: O(1)


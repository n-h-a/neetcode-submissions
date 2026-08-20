# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return head.next

# GOAL
# =========
# Given two sorted linked lists, merge them into one
# sorted linked list and return the head.

# BRUTE FORCE
# =========
# Keep pointers for both lists.
# For each position in the new list,
#   Pick the smaller element of the pointers.
#   Move the one you picked.
# Return the head.
# TC: O(N + M)
# SC: O(N + M)

# IDEA
# =========
# Why is brute force suboptimal?
#   It takes up O(N + M) auxiliary space when we allocate
#   a new array to store the result.
# Rather than using a new linked list to store, we just move around
# pointers. Use two pointers method.
#   Create a head pointer and a tail pointer. 
#   While lists still have elements,
#       If you get pointed at, your pointer moves up.
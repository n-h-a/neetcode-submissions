# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        p1 = list1
        p2 = list2
        head = ListNode()
        
        prev = head
        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    prev.next = p1
                    prev = p1
                    p1 = p1.next
                else:
                    prev.next = p2
                    prev = p2
                    p2 = p2.next
            elif p1:
                prev.next = p1
                break
            else:
                prev.next = p2
                break

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
#   Keep a pointer for each array.
#   Point head to smallest.
#   If you get pointed at, your pointer moves up.



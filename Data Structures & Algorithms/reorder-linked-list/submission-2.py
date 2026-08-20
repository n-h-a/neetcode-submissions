# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# GOAL
# ========
# Given the head of a singly-linked list,
# reorder the nodes s.t. it becomes [0, n-1, 1, n-2, 2, n-3, ...].

# BRUTE FORCE
# ========
# Store all the nodes in an array.
# Set one pointer to the beginning, left, and one at the end, right.
# While l < r,
#   Link nodes[i].next to nodes[j].
#   Increment i.
#   If i >= j, break.
#   Link nodes[j].next to nodes[i].
#   Decrement j.
# TC: O(N)
# SC: O(N)

# IDEA
# =========
# What makes brute force suboptimal?
#   We're using auxiliary space to construct this list.
# Observation:
#   The constructed list is just the first half with
#   the second half reversed embedded within it.
# We need to find the second half:
#   Use fast and slow pointer.
# We need to reverse the second half.
#   Use temps.
# We need to merge the first and second halves.
#   Use temps.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
# GOAL
# ========
# Given the beginning of a linked list, return true
# if there is a cycle. Otherwise, return false.

# BRUTE FORCE
# ========
# Keep a set of seen nodes.
# Loop through the nodes,
#   If unseen, add it to the set.
#   Otherwise, return true.
# Return false.
# TC: O(N)
# SC: O(N)

# IDEA
# ========
# Why is brute force suboptimal?
#   We use auxiliary space to keep track of nodes we've seen.
# Use two pointers: one fast and one slow.
#   If the slow one is ahead of the fast one, there is a cycle.
#   If the fast one reaches the end, there is no cycle.
# TC: O(N + time to catch slow), aka O(N)
# SC: O(1)
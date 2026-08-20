# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left, right = dummy, head
        
        # Move right n away from left
        while n > 0 and right:
            right = right.next
            n -= 1 

        # Move left and right while right is not at end
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

# GOAL
# ========
# Given the head of a linked list and an int n, remove the nth
# node from the end of the list.

# QUESTIONS
# ========
# Is the list singly-linked?

# BRUTE FORCE
# ========
# 1) Construct a reversed version by iterating through the list.
#    Then iterate n times and remove the nth node from reversed list.
#    Reverse the list one more time.
#    TC: O(N), SC: O(N)
# 2) Copy the list into an array. Remove the nth node from the
#    end of the array. Copy the list back into a linked list.
#    TC: O(N), SC: O(N)
# 3) Iterate through the entire list to find the size.
#    Calculate what the nth node from the end of the list would be,
#    then move another pointer starting at beginning to it, and remove. 
#    TC: O(N), SC: O(1)

# IDEA
# ========
# What makes brute force suboptimal?
#   Looping multiple times over list.
#   Using auxiliary space.
# How do we find the nth node from the end of list?
#   We don't know the size of the list.
#   We can't traverse backwards.
# The nth node from the end is just n away from the end.
#   We can have a slow pointer at the beginning and a fast
#   pointer n away from it. If we move the pointers until
#   the fast one reaches the end, the slow pointer will be
#   at the one we want to remove.
# We actually want the one before the one we want to remove.
#   We can use a dummy node to get rid of the edge case s.t.
#   the node we want to remove is the head.
# TC: O(N), O(1)




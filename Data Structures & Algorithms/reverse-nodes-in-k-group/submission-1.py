# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # the node before a group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next # node after a group

            # Reverse group.
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next # now last node in group we just processed
            groupPrev.next = kth # we set it to point to the start of new group
            groupPrev = tmp 
        
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


        
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

# IDEA
# =======
# Observations:
#   The beginning of first group points at the end of the next group.
# Why is brute force suboptimal?
#   We use an additional data structure, an array, to store the nodes.
# 

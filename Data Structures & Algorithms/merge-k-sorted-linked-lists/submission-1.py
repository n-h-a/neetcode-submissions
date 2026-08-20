# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        while True:
            # Find the minimum node amongst lists.
            minNode = -1
            for i in range(len(lists)):
                # If list is empty, move on.
                if not lists[i]:
                    continue
                # If at the start or we find a smaller node, update min.
                if minNode == -1 or lists[i].val < lists[minNode].val:
                    minNode = i

            # If lists are empty, break out of the loop.
            if minNode == -1:
                break
            
            # Add minNode to result.
            curr.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            curr = curr.next

        return res.next




# GOAL
# ========
# Given an array of k sorted linked lists
# return a sorted linked list that is a result of them merged.

# BRUTE FORCE
# ========
# Create a new array, nodes.
# Loop through each list and add the value to nodes.
# Sort nodes.
# Create a new linked list.
#   For each value, create a new node.
# Return the new linked list.
# TC: O(N log N)
# SC: O(N)

# IDEA
# =======
# Initialize result.
# Until all lists are empty,
#   Compare all the heads of the lists.
#   Attach the smallest node to result.
#   Move the chosen lists' pointer to the next node.
# Return result.
# TC: O(N*k)
# SC: O(1)



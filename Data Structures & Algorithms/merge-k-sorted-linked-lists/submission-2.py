# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        curr = res
        minHeap = []

        for l in lists:
            if l is not None:
                heapq.heappush(minHeap, NodeWrapper(l))

        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

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
# 
# Intialize result.
# Create a min-heap.
# For each non-empty linked list,
#   Push its head node into the heap.
# While the heap is not empty:
#   Pop the node with the smallest value from the heap.
#   Attach it to result.
#   If the node has a next, push the next node onto the heap.
# Return the result when the heap is empty.
# TC: O(N * log K)



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums: # O(N)
            heapq.heappush(min_heap, num) # O(log K)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # O(log K)

        return min_heap[0]

# GOAL
# =======
# Given an unsorted array of ints and an int k, return
# the kth largest element in the array.

# BRUTE FORCE
# =======
# Sort the array.
# Return the kth largest element.
# TC: O(N log N)
# SC: O(N) depending on the sorting algorithm.

# IDEA
# =======
# The kth largest element is the smallest of the largest k
#   elements. We can use a min heap of k elements:
# Heapify the array in a min heap, only accepting k elements.
# Return the top of the heap.
# TC: O(N log K)
# SC: O(K)


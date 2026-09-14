class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            diff = y - x
            if diff > 0:
                heapq.heappush(maxHeap, -diff)

        return 0 if not maxHeap else -maxHeap[0]

# GOAL
# ======
# Given an array of stone weights, simulate:
#   1) Choose two heaviest stones w/ weights x and y
#   2) If same weight, remove both
#   3) If diff, remove smaller stone and make
#      the bigger one's weight the difference

# BRUTE FORCE
# ======
# Find the two heaviest weights.
# If same, get rid of both. 
# Otherwise, remove both and add the difference.
# TC: O(N^2 log N)

# IDEA
# ======
# The issue with brute force is sorting.
# Is there a way we can easily retrive and maintain
# a sorted order without sorting every time? Max heap.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if largest > second:
                heapq.heappush(max_heap, -(largest - second))

        if len(max_heap) != 0:
            return -max_heap[0]
        return 0

# GOAL
# ========
# * Find the two heaviest stones:
#       If equal weight, destroy both.
#       If different, smaller stone is destroyed while
#           bigger stone weighs the positive difference.

# BRUTE FORCE
# ========
# While len(stones) > 1:
#   Loop through the array to find the two heaviest stones.
#   Perform the smash.
# TC: O(N^2)
# SC: O(1)

# OBSERVATIONS
# ========
# * Why is brute force suboptimal?
#       We are repeatedly looking through the array to
#       find the two heaviest stones.

# IDEA
# ========
# To keep track of the two heaviest stones, we can
#   use a max heap. 
# Create a max heap.
# While len(stones) > 1:
#   Pop the heap twice for the two heaviest stones.
#   Perform the smash.
# TC: O(N log N)
# SC: O(N)

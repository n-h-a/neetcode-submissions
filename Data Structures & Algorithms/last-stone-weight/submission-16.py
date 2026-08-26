class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x < y:
                heapq.heappush(max_heap, x - y)

        return 0 if not max_heap else -1 * max_heap[0]

        
# GOAL
# ========
# Given an integer array, choose the two largest ints, x and y.
#   If equal, remove both.
#   If x < y, remove x and set y to their difference.
# Return the last remaining int or 0 if none remain.

# BRUTE FORCE
# ========
# while len(stones) > 1:
#   sort the array
#   grab the first two stones
#       perform the simulation
# return 0 if not stones else stones[0]
# TC: O(N^2 log N)
# SC: O(N)

# OBSERVATIONS
# ========
# Why is brute force suboptimal?
#   We sort the array at every iteration which adds overhead.
# => Need to find a way to keep track of max stones => max heap.

# IDEA
# ========
# Use a max heap to keep track of the two heaviest stones at each simulation step.
# Heapify the array.
# While the len(heap) > 1: 
#   Pop heap twice for x and y.
#   If x > y:
#       Push difference onto max heap.
# Return 0 if not max heap else top of heap.
# TC: O(N log N)
# SC: O(N)
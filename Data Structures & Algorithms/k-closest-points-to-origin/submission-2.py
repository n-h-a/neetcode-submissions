class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda p: p[0]**2 + p[1]**2

        min_heap = [(dist(p), p) for p in points]
        heapq.heapify(min_heap)

        res = []
        for i in range(k):
            priority, point = heapq.heappop(min_heap)
            res.append(point)

        return res

# GOAL
# =======
# Given a list of coords and int k, return the k
# closest points to the origin.

# BRUTE FORCE
# =======
# Sort the coords by Euclidean distance.
# Return the first k.
# TC: O(N log N)
# SC: O(N)

# IDEA
# =======
# Construct a min heap of the points.
# Pop the smallest k.
# TC: O(N + k log N))
# SC: O(N)

        
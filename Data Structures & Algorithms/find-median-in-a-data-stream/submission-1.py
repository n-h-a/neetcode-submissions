class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # Ensure all small nums <= all large nums.
        if (self.small and self.large) and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Ensure size is balanced.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2
        
# GOAL
# =======
# Implement a MedianFinder class that supports three methods:
#   Constructor     initializes
#   addNum(num)     adds num to the data structure
#   findMedian()    returns the median so far

# BRUTE FORCE
# =======
# Constructor
#   Use a list for the data structure.
# addNum(num)
#   Append the element to the list. --> O(1)
# findMedian()
#   Sort the list, then return the median using indexing. --> O(N log N)

# IDEA
# =======
# Why is brute force suboptimal?
#   We sort the list every time we call findMedian.
# We can split the data structure into two parts:
#   The left half and the right half.
# We use two heaps (one min and one max) to find median:
#   We always add the number to small (just convention).
#   Ensure all small nums <= large nums.
#   Ensure size is balanced between heaps.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
# BRUTE FORCE
# ========
# __init__
#   Initialize a list attribute for nums.
# add
#   Append the value to the list, sort, then
#   return the element at length of list - k.
# TC: O(M * N log N) s.t. M is # of calls made to add()

# IDEA
# ========
# Use a min-heap to maintain the kth largest elements seen so far.
# __init__
#   Initialize a min heap for nums.
# add
#   If adding the new number to the heap exceeds k,
#       Remove the smallest element.
#   Return the new top.
# TC: O(M * log K) s.t. M is # of calls made to add()
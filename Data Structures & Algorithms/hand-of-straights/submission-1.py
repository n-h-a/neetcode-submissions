class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        
# GOAL
# =======
# Given an array of ints and a groupSize, return 
# true if possible to rearrange the cards into groups of size groupSize s.t. the elements in each group are consecutive.

# BRUTE FORCE
# =======
# Sort the array.
# Greedily create groups of size groupSize.
#   If you can't find consecutive item, return False.
# TC: O(N^2), SC: O(N)

# IDEA
# =======
# Use a hash map to count frequency of numbers and 
# a min heap to keep track of the minimum start.
# Count frequency of numbers.
# Heapify keys of count.
# While heap is not empty:
#   See if first of heap can be a start to a group.
#   For i in range(first, first + groupSize):
#       If i not in count, return False.
#       Decrement count.
#       If count is now 0, we need to remove it
#           from min heap. If it is not at the
#           top of the min heap, we return false.
#           Otherwise, pop it from the minHeap.
# Return True.
# TC: O(N log N)
# SC: O(N)

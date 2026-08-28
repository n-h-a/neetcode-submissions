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

# OBSERVATIONS
# =======
# * Bc we want consecutive numbers, sorting makes sense. 


# IDEA
# =======
# Use a hash map to count frequency of numbers.
# Sort the array.
# Loop through sorted array:
#   


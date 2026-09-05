class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for num in hand:
            freq[num] = 1 + freq.get(num, 0)

        minH = list(freq.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for num in range(first, first + groupSize):
                if num not in freq:
                    return False
                freq[num] -= 1

                if freq[num] == 0:
                    if num != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        
# GOAL
# =======
# Given an int array and groupSize, return true if it is possible
# to rearrange the cards into consecutive groups of size, groupSize.

# BRUTE FORCE
# =======
# Sort the list and starting from end, we create groups by
# searching for an element that's one less than the one we
# previously added to groups.
# TC: O(N^2), SC: O(N)

# OBSERVATIONS
# =======
# * We just need to know if the next one we want exists.
# * We also need to know the smallest available number.

# IDEA
# =======
# * Use a hashmap to count frequency of ints.
# * Use a min heap to keep track of the smallest available number.
# Create a frequency map.
# Create a min heap of all available numbers.
# While the min heap still has elements,
#   Grab the first. This will start our group.
#   For every number (including the first) to first + groupSize,
#       Check if we still have it in the list using the frequency map.
#           If not return false.
#       If yes, then we decrement.
#       If the count for the number becomes 0, then we need to remove it 
#       from our min heap of available numbers.
#           However, the number should be the most recent one.
#           If it is not the top of the heap, return False.
# If the min heap becomes empty and we haven't encountered any issues,
# return True.
# TC: O(N log N), SC: O(N)








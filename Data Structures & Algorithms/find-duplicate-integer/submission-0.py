class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
                
# GOAL
# =======
# Given an array of ints size n + 1 s.t. every int is
# within the range [1, n], return the repeated integer.

# BRUTE FORCE
# =======
# Use a hashset to keep track of seen integers.
# Iterate through the array:
#   If int seen, return int.
#   Otherwise, we add to hashset.
# TC: O(N), O(N)

# OBSERVATIONS
# =======
# The numbers are within the range [1, n].
# So, we can treat the array like a linked list,
#   where each index points to the next.

# IDEA
# =======
# Treat the array like a linked list, where
#   each index points to the next.
# Because one number is duplicated, two indices
#   will point to the same index, creating a cycle.
# Use Floyd's fast & slow pointer technique:
#   Slow pointer moves by one. Fast moves by two.
#   If there exists a cycle, they will meet.



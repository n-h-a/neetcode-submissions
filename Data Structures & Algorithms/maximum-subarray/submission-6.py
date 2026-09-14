class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_total = nums[0]
        for num in nums:
            if total < 0:
                total = 0
            total += num
            max_total = max(max_total, total)

        return max_total


# GOAL
# =======
# Given an array of ints, find the subarray
# with the largest sum and return the sum.

# BRUTE FORCE
# =======
# For each integer,
#   Explore all subarrays.
#   Keep track of largest sum.
# TC: O(N^2)
# SC: O(1)

# OBSERVATION
# =======
# * Taking a negative is not always bad b/c it can lead
#   to a bigger sum.
# * If my sum becomes negative at some point, my resulting
#   subarray should start after b/c adding a negative sum
#   to any future subarrays doesn't help.

# IDEA
# =======
# If sum becomes negative, reset sum. Otherwise, keep adding.


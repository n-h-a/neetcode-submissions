class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            n_sum = numbers[left] + numbers[right]
            if n_sum > target:
                right -= 1
            elif n_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []

# GOAL
# ==========
# Return the indices (1-indexed) of two numbers with the sum of target.
# - Use O(1) additional space.

# BRUTE FORCE
# ==========
# For every number, loop through list again to find pair that adds up to sum.
# TC: O(N^2)
# SC: O(1)

# OBSERVATIONS
# ==========
# Array is sorted in non-decreasing order.

# IDEA
# ==========
# OVERVIEW: Because the array is sorted in non-decreasing order,
# you can check both ends, making minimal decisions based on the
# sum of those ends until you find your answer.
# Two pointer approach, starting at ends.
# If sum of ends > target,
#   Move right pointer down.
# If sum of ends < target,
#   Move left pointer up.

# PSEUDOCODE
# ==========
# Initialize pointers.
# While left <= right,
#   Find sum of left + right.
#   If sum > target, decrement right pointer.
#   elif sum < target, increment left pointer.
#   else, return [left + 1, right + 1].


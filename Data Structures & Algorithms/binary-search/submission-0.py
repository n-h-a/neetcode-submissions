class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid

        return -1

# GOAL
# ========
# Return index of target if found. Return -1 otherwise.

# BRUTE FORCE
# ========
# For every number in list,
#   Check if it equals target. 
#       If yes, return index.
# If target not in list, return -1.
# TC: O(N)
# SC: O(1)

# IDEA
# ========
# Since list is sorted, we can limit the range by choosing an element and comparing.
#   EX: If the element chosen has value 6 and target is 4, target can't be found to
#   the right of the element we chose. Therefore, we can eliminate every element after.
# Where is the best element to pick?
#   The middle. It eliminates our choices by half every time.
# IDEA:
#   Start with a big range.
#   Pick the middle and compare.
#   Adjust range depending on comparison.

# PSEUDOCODE
# ========
# Initialize left and right pointers.
# While left is not past the right,
#   Pick midpoint.
#   If midpoint < target,
#       Move left pointer to target.
#   If midpoint > target,
#       Move right pointer to target.
#   If midpoint == target,
#       Return index.
# Return -1.
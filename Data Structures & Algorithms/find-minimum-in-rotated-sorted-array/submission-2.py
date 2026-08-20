class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while nums[lo] > nums[hi]:
            mid = lo + (hi - lo) // 2

            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]

        
# GOAL
# ========
# Return the minimum element of the array after
# it has been rotated k times.

# NOTES
# ========
# All elements are unique.
# Do all elements have to be consecutive? No.

# BRUTE FORCE
# ========
# Keep min variable.
# For every num in nums,
#   Update min variable if num < min.
# Return min.
# TC: O(N)
# SC: O(1)

# IDEA
# ==========
# What makes brute force suboptimal?
#   We're checking every element of the list, even though
#       we know that, if the next element is < current,
#       the next is the min.
#   Because the search space is sorted,
#       we can actually eliminate half of it at every
#       iteration using binary search.
# The issue here is rotation.
#   A smaller num could be found on the left of another.
#   A bigger num could be found on the right of another.
# How do we know which side to eliminate?
#   If the ends are out of order, we know the search space
#       contains two sorted splits.
#   If we pick a mid, we can see which search space it belongs to.
#   We want to pick the side that will have smaller elements,
# TC: O(log N)
# SC: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            target_big = target >= nums[0]
            mid_big = nums[mid] >= nums[0]

            if target_big != mid_big:
                if target_big:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
   
        return -1

        
# GOAL
# ========
# Return the index of target if in nums. 
# Otherwise, return -1.

# BRUTE FORCE
# =========
# For every num in nums,
#   Check if it is target. If it yes, return the index.
# Return -1 if target not found.
# TC: O(N)
# SC: O(1)

# IDEA
# =========
# Why is brute force suboptimal?
#   Because the array is in order, we don't really have to check 
#   every single element. We can limit the range.
# Because the array still maintains a sorted order,
#   we can use binary search.
# What does a rotated array look like?
#   The beginning > end.
#   Two sorted parts: 1) larger nums, 2) smaller nums
# Notes
#   If target < beginning,
#       then it isn't a part of the larger nums.
#   If target >= beginning,
#       then it is a part of the larger nums.
#   But we need to limit the range: We pick a midpoint.
#       If the midpoint < beginning,
#           then it isn't a part of the larger nums.
#       If the midpoint >= beginning,
#           then it is a part of the larger nums.
#   We need midpoint and target to be in the same part.
#       If same part, we can use normal binary search.
#           If mid > target, hi = mid - 1
#           If mid < target, lo = mid + 1
#       Otherwise, we just limit space to section that target is in.
#           If target is in big part,
#               hi = mid - 1
#           Otherwise,
#               lo = mid + 1
# TC: O(log N)
# SC: O(1)
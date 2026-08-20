class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1

        total = len(A) + len(B)
        half = total // 2

        lo = 0
        hi = len(A)
        while lo <= hi:
            numAs = lo + (hi - lo) // 2 # number of elements we take from A
            numBs = half - numAs # number of elements we take from B

            # Boundary trick: To preserve comparison, we pretend that,
            # if no values to left (or right), then that end is just the
            # smallest (or biggest) number.
            maxAL = A[numAs - 1] if numAs > 0 else float("-infinity")
            minAR = A[numAs] if numAs < len(A) else float("infinity")
            maxBL = B[numBs - 1] if numBs > 0 else float("-infinity")
            minBR = B[numBs] if numBs < len(B) else float("infinity")

            # Check if partition is valid.
            if maxAL <= minBR and maxBL <= minAR:
                if total % 2:
                    return min(minAR, minBR)
                return (max(maxAL, maxBL) + min(minAR, minBR)) / 2
            elif maxAL > minBR:
                hi = numAs - 1
            else:
                lo = numAs + 1




# GOAL
# =========
# Given two sorted arrays, return the median of both arrays combined.

# QUESTIONS
# =========
# Are elements unique?
# Is the sort strictly ascending?

# BRUTE FORCE
# =========
# Create an array of size N and M.
# Use two pointers starting at the beginning of each array.
# Construct new array, preserving order.
# Return the median.
# TC: O(N + M)
# SC: O(N + M)

# IDEA
# =========
# Why is brute force suboptimal?
#   * We use extra space to track the median.
#   * Because the array is sorted, we may be able to search
#     quicker by eliminating ranges.
# Observations:
#   * The combined array can be divided into two parts:
#       1) has median + contains elements from left partitions of both arrays
#       2) contains elements from right partitions of both arrays
#   * Once the left partitions are identified, the median is the max value.
#   * The left partitions altogether have to be < size (combined array).
# Idea:
#   * Binary search on arrays to find the cuts for a valid
#     overall left partition.
#   * However, we just need to cut / search one because
#     we know the total # of elements for left partition is
#         1/2 of overall = left partition of array 1
#                        + left partition of array 2.
#   * We pick the smaller array to binary search for efficiency.
#   * We need to determine if the cut is valid.
#     If array 1 is partitioned  | A | B | 
#                               a1 a2 b1 b2
#        array 2 is partitioned  | C | D |
#                               c1 c2 d1 d2
#     And, for example, a1, a2 are endpoints of A, then
#     this is required:
#       a2 <= b1 and a2 <= d1
#       c2 <= b1 and c2 <= d1
#     It's a given that a1 <= b1 and c2 <= d1, so we just check
#       a2 <= d1 and c2 <= b1.
#     In sum,
#       If a2 <= d1 and c2 <= b1,
#           Return the median. Depends on if size(overall) is odd / even.
#       elif a2 > d1,
#           We need to shrink to take more elements of second array.
#       else c2 > b1,
#           We need to expand to take less elements of second array.
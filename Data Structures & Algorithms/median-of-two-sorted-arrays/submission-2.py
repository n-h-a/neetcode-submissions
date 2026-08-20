class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def median_range(arr, l, r):
            n = r - l + 1
            mid = l + n // 2

            if n % 2:
                return arr[mid]
            return (arr[mid - 1] + arr[mid]) / 2

        def brute_force_range(a, al, ar, b, bl, br):
            merged = []

            i, j = al, bl

            while i <= ar and j <= br:
                if a[i] <= b[j]:
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1

            while i <= ar:
                merged.append(a[i])
                i += 1

            while j <= br:
                merged.append(b[j])
                j += 1

            n = len(merged)
            if n % 2:
                return float(merged[n // 2])
            return (merged[n // 2 - 1] + merged[n // 2]) / 2

        def solve(a, al, ar, b, bl, br):
            len_a = ar - al + 1
            len_b = br - bl + 1

            if len_a <= 0:
                return median_range(b, bl, br)

            if len_b <= 0:
                return median_range(a, al, ar)

            if len_a + len_b <= 4:
                return brute_force_range(a, al, ar, b, bl, br)

            ma = median_range(a, al, ar)
            mb = median_range(b, bl, br)

            if ma == mb:
                return float(ma)

            k = min(len_a, len_b) // 2

            if ma < mb:
                # discard lower k elements of a
                # discard upper k elements of b
                return solve(a, al + k, ar, b, bl, br - k)
            else:
                # discard upper k elements of a
                # discard lower k elements of b
                return solve(a, al, ar - k, b, bl + k, br)

        return solve(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1)

# GOAL
# =========
# Given two sorted arrays, return the median among both.

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
#   * It seems like the median of both arrays is nested in between
#     the medians of each. Why is that the case?
#       As # of elements in the overall list increases, so does the overall median.
#       Medians of each never move backwards b/c combining lists only adds more
#           elements before it. It doesn't take away any elements.
#   * The median overall is the median of the space between the two.
# Since the overall median will be in between the medians of each, we know...
#     smaller median < overall median < larger median
# 

# 2 LISTS
# A | B 
# C | D 

# CASE 1: Lists do not mix.
# A | B  C | D 
# C | D  A | B 
# What's the median?
#   If N + M odd, then it'll be either the last or first elem of the odd array.
#   If N + M even, then (last elem of first + first elem of second) / 2.



# CASE 2: AC mix
# AC B D
# A C B D
# It pushes the medians of both A and C right. Why?
#   B/c we're adding elements to the left of each median.
#   (The earlier median may stay in the same spot).

# CASE 3: BD mix
# A C BD
# A C B D

# [1, 2, 3, 7, 8, 9, 10, 11, 12] 
# [4, 5, 6]      
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#              s        f
#                   M

# [5, 6] -> 5.5
# [7, 8] -> 7.5


# [1, 2, 6] -> 2
# [3, 5] -> 4
# [1, 2, 3, 5, 6]
#     f    s


# If overall array is even, 
#   we need to return two indices.
# Otherwise, 
#   return just one.

# Find the medians of the two search spaces.
# Use binary search to limit search space to valid nums:
#   For smaller median search space (right of),
#       Search for largest number < larger median.
#   For larger median search space (left of),
#       Search for smallest number > smaller median.





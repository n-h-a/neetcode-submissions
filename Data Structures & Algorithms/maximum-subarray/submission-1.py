class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = nums[0], 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

        

# GOAL
# =======
# Given an int array, find the subarray with the largest
# sum and return the sum.

# BRUTE FORCE
# =======
# Generate all subarrays, and return the min sum.
# TC: O(N^2)
# SC: O(1)

# IDEA
# =======
# Use Kadane's Algorithm:
#   If the running sum becomes negative, keeping it will only
#       reduce the sum of any future subarray. Start a new one.
#   Otherwise, continue.
# TC: O(N)
# SC: O(1)


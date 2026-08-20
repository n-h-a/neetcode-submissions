class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        max_len = 0
        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                max_len = max(length, max_len)
            
        return max_len

# GOALS
# =========
# Return the length of the longest consecutive sequence.

# BRUTE FORCE
# =========
# Sort and perform greedy algorithm.
# TC: O(N log N)

# IDEA
# =========
# Go through list once, putting everything in hash set.
# Go through list again
#   If num - 1 is not in hash set, don't build sequence. 
#   Otherwise, build sequence.
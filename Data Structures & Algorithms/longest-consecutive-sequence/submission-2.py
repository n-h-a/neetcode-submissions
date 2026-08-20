class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()

        length = 0
        max_len = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] == (nums[i + 1] - 1):
                length += 1
            else:
                length = 0

            max_len = length if length > max_len else max_len

        return max_len + 1
        

# GOALS
# =========
# Return the length of the longest consecutive sequence.

# BRUTE FORCE
# =========
# Sort and perform greedy algorithm.
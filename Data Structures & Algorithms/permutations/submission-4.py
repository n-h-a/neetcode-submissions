class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtrack(i, nums):
            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1, nums)
                nums[i], nums[j] = nums[j], nums[i]
        
        backtrack(0, nums)
        return res


# GOAL
# ========
# Given an array of unique integers, return all the possible
# permutations.

# IDEA
# ========
# For each index i, we consider putting every remaining element from
# i onward in that position, then explore the path starting from there.
# Switch the element back after done.
# TC: O(N * N!)
# SC: O(N * N!)



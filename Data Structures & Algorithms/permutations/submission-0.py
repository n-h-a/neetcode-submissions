class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

# GOAL
# ========
# Given an array of unique integers, return all the possible
# permutations.

# IDEA
# ========
# For each position, we consider two options for each number:
#   1) Number goes there
#   2) Number doesn't go there



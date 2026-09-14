class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1
        return res

# GOAL
# ========
# Given an array of max jump lengths, return
# min # of jumps needed to reach last position.

# OBSERVATION
# ========
# * We want to keep picking the optimal soln. But how?
# * For each jump we pick, we get a range of choices.
#       We need to keep track of which choice brings us
#       the furthest, and that will create a new range.
# * The number of ranges is our answer.

# IDEA
# ========
# For each jump, keep track of how 
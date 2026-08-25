
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
# GOAL
# =======
# Given an int array nums s.t. each element is a jump 
# length, return true if you can reach the last index 
# starting 0. Otherwise, return False.

# IDEA
# =======
# Think about the problem in reverse:
#   Consider which positions will eventually reach the goal.
#   Move backward to see if earlier positions can reach the goal.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        while pos < len(nums) - 1:
            if nums[pos] == 0:
                return False

            if pos + nums[pos] >= len(nums) - 1:
                return True
            
            next_best_pos = pos + 1
            next_best_reach = next_best_pos + nums[next_best_pos]

            for i in range(1, nums[pos] + 1):
                candidate_pos = pos + i
                if candidate_pos >= len(nums):
                    break

                candidate_reach = candidate_pos + nums[candidate_pos]

                if candidate_reach > next_best_reach:
                    next_best_reach = candidate_reach
                    next_best_pos = candidate_pos
            pos = next_best_pos

        return True
        
# GOAL
# =======
# Given an int array nums s.t. each element is a jump 
# length, return true if you can reach the last index 
# starting 0. Otherwise, return False.

# OBSERVATIONS
# =======
# We want to get TO or PAST the last index.
# We don't have to jump the max length every time.

# IDEA
# =======
# At every step, we want to jump the max amount of times.
# While we're not at the end and current jump length != 0,


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        N = len(nums)
        for i in range(N - 2):
            l = i + 1
            r = N - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                t_sum = nums[l] + nums[r]
                target = -nums[i]
                if t_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif t_sum > target:
                    r -= 1
                else:
                    l += 1

        return res

        
# GOAL
# =========
# Return all the unique triplets that add up to 0.

# BRUTE FORCE
# =========
# For each num a,
#   For each num b thereafter,
#       For each num c thereafter,
#           If a, b, c sum up to 0,
#               Add to result
# TC: O(N^3)
# SC: O(1)

# OBSERVATIONS
# =========
# O(N log N) < O(N^2), so we can achieve O(N^2) with sorting.
# After sorting list, you can do two pointer technique s.t. current num is target.

# IDEA
# =========
# Sort nums.
# For every num,
#   Conduct two-sum technique.
#       Create l and r pointers.
#       Find sum of vals at l and r.
#       If sum == num,
#           Add triplet to res.
#       elif sum > num,
#           Increment l.
#       elif sum < num,
#           Decrement r.
# Return res.
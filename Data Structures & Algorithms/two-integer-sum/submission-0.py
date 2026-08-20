class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices:
                return [indices[diff], i]
            else:
                indices[nums[i]] = i

        return []


# IDEA:
# Keep dictionary for corresponding pairs and their indices.
# Loop through list,
#   Check if num's pair is in list.
#       If yes, return indices.
#       Otherwise,
#           Add curr num to list.
        
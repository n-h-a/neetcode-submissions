class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

# OBSERVATIONS:
# TC: O(N)

# PSEUDOCODE:
# For every original element, append the element to the array.
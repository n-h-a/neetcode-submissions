class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in positions:
                return [positions[diff], i]
            else:
                positions[nums[i]] = i

        return []
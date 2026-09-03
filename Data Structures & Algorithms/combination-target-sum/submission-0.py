class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

# IDEA
# ========
# Build all combinations of numbers that add up to target
# by making a decision for every index:
#   1) Include the current number
#   2) Skip the current number

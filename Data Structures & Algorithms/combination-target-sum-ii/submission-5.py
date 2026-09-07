class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        total = 0

        candidates.sort()
        def dfs(i):
            nonlocal total

            if target == total:
                res.append(combo.copy())
                return
            
            if i >= len(candidates) or total + candidates[i] > target:
                return

            combo.append(candidates[i])
            total += candidates[i]
            dfs(i + 1)

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            combo.pop()
            total -= candidates[i]
            dfs(i + 1)
        
        dfs(0)
        return res


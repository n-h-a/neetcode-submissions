class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)

        res = [0] * N
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res


# GOAL
# =========
# Return an array result s.t. result[i] == # of days after the
# ith day before a warmer temp appears.

# BRUTE FORCE
# =========
# For every temperature,
#   Loop through the list again and keep count of how many
#   temps until a warmer one appears.
# TC: O(N^2)
# SC: O(1)

# IDEA
# ==========
# Why is brute force suboptimal?
# Use a stack. Keep stack monotonically increasing.
#   Traverse list in reverse order.
#   Stack holds indices.
# While stack exists and top of stack < num,
#   Pop and add count of popped.
# If stack exists, add 1 to count. Otherwise, set count to 0.
# Add num to stack. 






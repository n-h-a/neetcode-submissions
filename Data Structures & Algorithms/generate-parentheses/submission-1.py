class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                res.append("".join(stack))
                return

            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClose)
                stack.pop()
            if numClose < numOpen:
                stack.append(")")
                backtrack(numOpen, numClose + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        
# GOAL
# =======
# Given an integer n, return all well-formed parentheses
# strings you can generate with n pairs of parentheses.

# IDEA
# =======
# Each result string should have 2 * n characters or elements,
# Use backtracking: For each index (2 * n), consider:
#   1) Adding an open parentheses
#       We can only do this IFF numOpen < n.
#   2) Adding a closed parentheses.
#       We can only do this IFF numClose < n.
# This is backtracking but some paths are blocked if they do not
# satisfy the condition.
# TC: O(4^N / sqrt(N))
# SC: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[c] != top:
                    return False
        if not stack:
            return True
        return False


# GOAL
# =========
# Return true if s is a valid string. Otherwise, return false.

# BRUTE FORCE
# =========
# While (), [], or {} in the string,
#   Remove them.
# TC: O(N^2)

# IDEA
# =========
# We need to find the counterpart of the most recent
# open symbol we've seen.
#   Use a stack to keep track of the LIFO order.
# Could stack be not empty after for loop without returning false?
#   Yes, if the string only has open symbols.
# What if the string only had closed symbols?
#   Need to check if the stack is empty.
# Use dictionary to check corresponding pair.

# PSEUDOCODE
# =========
# For each char in string,
#   If it is an open symbol, add it to the stack.
#   If it is a close symbol,
#       If stack empty, return False.
#       Check if the top of the stack corresponds.
#           If yes, pop top.
#           Otherwise, return false.
# If stack not empty, return false. Otherwise, return true.
# TC: O(N)
# SC: O(N)
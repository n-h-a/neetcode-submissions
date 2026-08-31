class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen = 0, 0
        for c in s:
            if c == '(':
                minOpen += 1
                maxOpen += 1
            elif c == ')':
                minOpen -= 1
                maxOpen -= 1
            elif c == '*':
                minOpen -= 1
                maxOpen += 1
            
            if maxOpen < 0:
                return False
            
            minOpen = max(minOpen, 0)
        return minOpen == 0

# GOAL
# =======
# Given a string of only either '(', ')', or '*', return true
# if it is a valid parentheses string.

# BRUTE FORCE
# ========
# Try every single possibility when reaching an asterisk.
# TC: O(3^N), but O(N^3) with memoization

# OBSERVATIONS
# ========
# * Every open parenthesis needs to have a following closing parenthesis.
# * We want to ensure that:
#       1) There are enough open parentheses
#       2) There are no open parentheses left over

# IDEA
# ========
# Use two variables: one tracking minOpen parentheses and one tracking maxOpen parentheses that we have to deal with.
# For each char in the string,
#   If the char is '(', increment both variables.
#   If the char is ')', decrement both variables.
#   If the char is '*', increment max, decrement min.
#   If max becomes negative, return false b/c
#       that means that we have too few open parentheses.
#   If min becomes negative, reset it to 0 b/c we can't have
#       unmatched ')' without '('
# If minOpen is 0, it means all '(' are matched with ')'.
# TC: O(N), SC: O(1)
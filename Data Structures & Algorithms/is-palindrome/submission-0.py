class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
        

# GOAL
# ========
# Given a string, return true if it's a palindrome. Otherwise return false.

# IDEA
# ========
# Use two pointers starting at left and right to iterate
# through string and check if palindrome.
# Skip non-alphanumeric.
# TC: O(N)
# SC: O(1)

# PSEUDOCODE
# ========
# Construct two pointers, pointing at ends.
# While left <= right,
#   If left points at non-alphanumeric, increment it.
#   If right points at non-alphanumeric, decrement it.
#   Otherwise,
#       Compare values at two pointers.
#       If not same, return False.
# Return True.
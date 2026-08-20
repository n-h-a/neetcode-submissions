class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            left = s[l]
            right = s[r]
            
            if not left.isalnum():
                l += 1
                continue
            
            if not right.isalnum():
                r -= 1
                continue

            if left.lower() != right.lower():
                return False

            l += 1
            r -= 1

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
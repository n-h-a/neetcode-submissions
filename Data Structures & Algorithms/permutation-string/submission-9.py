class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        f_s1 = {}
        f_window = {}
        for c in s1:
            f_s1[c] = f_s1.get(c, 0) + 1

        for r in range(len(s2)):
            right_char = s2[r]
            f_window[right_char] = f_window.get(right_char, 0) + 1

            if (r - l + 1) > len(s1):
                left_char = s2[l]
                f_window[left_char] -= 1

                if f_window[left_char] == 0:
                    del f_window[left_char]

                l += 1
            
            if f_window == f_s1:
                return True
                
        return False

        
    

# GOAL
# =========
# Return true if s2 contains a permutation of s1.
# Otherwise return false.

# BRUTE FORCE
# =========
# For each substring in s2 - O(M^2),
#   For each letter in s1,
#       Check if it has same exact characters as s1.
#       Return True. 
# Return False.
# TC: O(N * M^2)
# SC: O(1)

# IDEA
# =========
# Why is brute force suboptimal?
#   It checks every substring, even when we already know...
#       there exists a character that isn't in s1
#       the substring isn't the same length as s1
#   We only care about substrings s.t. len(substring) == len(s1).
# How do we solve this?
#   Can keep a sliding window that maintains at most len(s1).
#       If window size becomes bigger than len(s1), remove s2[l]
#       and move l.
#       Whenever window size equals len(s1), compare counts.

# PSEUDOCODE
# =========
# Count characters in s1
# Move r across s2
# Add s2[r] into a window count
# If window size becomes bigger than len(s1), remove s2[l] and move l
# Whenever window size equals len(s1), compare counts






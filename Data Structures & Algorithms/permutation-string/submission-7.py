class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0

        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        t_freq = freq.copy()

        while r < len(s2):
            letter = s2[r]
            if letter not in t_freq:
                t_freq = freq.copy()
                l += 1
                r = l
            else:
                if t_freq[letter] == 1:
                    del t_freq[letter]
                else:
                    t_freq[letter] -= 1

                if (r - l + 1) == len(s1) and not t_freq:
                    return True
                r += 1
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
#   If we encounter a character that isn't in s1,
#       We move the window to start one after where
#       the unshared character is found.

# PSEUDOCODE
# =========
# l = 0
# r = 0
# Build frequency map for s1, freq_s1
# Make copy of freq_s1, temp_freq_s1,
# while r < len(s2):
#   if r - l + 1 == len(s1) and not temp_freq_s1:
#       return True
#   if s2[r] is not a letter in temp_freq_s1,
#       reset temp_freq_s1
#       move l and r to r + 1
#   otherwise
#       move r
#       if temp_freq_s1[r] == 1, delete temp_freq_s1[r]
#       otherwise, just subtract count
# return false






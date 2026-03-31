class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for c in t:
            if c not in freq:
                return False
            else:
                freq[c] -= 1;
                if freq[c] < 0:
                    return False

        return True
        

# OBSERVATIONS
# 1) If strings are different lengths, return False.
# 2) Anagram ==> every letter in s appears the same amount of times in t
# 3) At least, TC is O(N).

# PSEUDOCODE
# 1) For each letter in s, count # occurrences.
# 2) For each letter in t,
#       If letter not stored, return false.
#       If letter in freq, subtract 1.
#           If # occurrences < 0, return false.


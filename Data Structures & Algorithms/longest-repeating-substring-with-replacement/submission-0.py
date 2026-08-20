class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, max_len = 0, 0, 0
        freq = defaultdict(int)
        max_freq = 0
        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len


# GOAL
# ========
# Return the length of the longest substring
# containing only one character.

# OBSERVATIONS
# ========
# The best character to replace with is most frequent one.
#   (Length of substring - max frequency) is the number of
#   changes you need to make. If this > k, the substring is invalid.

# BRUTE FORCE
# ========
# For every substring - O(N^2),
#   Build frequency map by scanning the substring - O(N)
#   Let max_freq be the highest character frequency in that substring.
#   If substring is valid (substring_length - max_freq <= k):
#       Update longest length.
# TC: O(N^3)
# SC: O(P) s.t. P is number of unique characters in string.

# IDEA
# ========
# How is brute force suboptimal?
#   We're doing a lot of extra work:
#       * Building new frequency map for substring
#       * Trying every substring
# We don't need to build a new frequency map for every
#   substring because the bigger ones are made of the smaller
#   ones, and we already did the work for the smaller ones.
# We don't need to try every substring because
#   once a window is invalid, making it bigger will not
#   make it valid unless you move the left side up.
# Use sliding window approach s.t.
#   If window is invalid [len(substring) - max freq > k]:
#       Shrink window by moving left.
#   Expand window.
# TC: O(N)
# SC: O(P) s.t. P is # of unique chars.




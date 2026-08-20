class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tfreq, wfreq = {}, {}
        for c in t:
            tfreq[c] = tfreq.get(c, 0) + 1

        have, need = 0, len(tfreq)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            wfreq[c] = wfreq.get(c, 0) + 1
        
            if c in tfreq and wfreq[c] == tfreq[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                wfreq[s[l]] -= 1
                if s[l] in tfreq and wfreq[s[l]] < tfreq[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        
# GOAL
# ========
# Return shortest substring of s s.t. every letter in t
# is in that substring. If DNE, return "".

# BRUTE FORCE
# =========
# For every substring in s -- O(N^2),
#   Check if it has every letter in t.
# TC: O(N^2 * (N + M)) --> ~O(N^3)

# IDEA
# =========
# Why is brute force suboptimal?
#   We're doing a lot of extra work. If we know one bigger substring
#   x does not contain every character in t, then every substring of
#   x also doesn't.
# Expand window until you find all letters in t.
# Shrink window until you don't have all letters in t,
#   then update min_s.


# PSEUDOCODE
# =========
# l = 0
# min_s = ""
# Construct tfreq.
# Construct wfreq.
# for r in range(len(s)):
#   add s[r] to wfreq.
#   while wfreq == treq:
#       decrement wfreq at s[l]
#       decrement l
#   min_s = s[l - 1:r]
# return min_s
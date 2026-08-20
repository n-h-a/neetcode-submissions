class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occur = {}

        for c in s:
            if c in occur:
                occur[c] += 1
            else:
                occur[c] = 1

        for c in t:
            if c in occur:
                occur[c] -= 1
                if occur[c] < 0:
                    return False
            else:
                return False

        return True
        
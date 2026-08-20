class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur = {}

        for c in s:
            if c in occur:
                occur[c] += 1
            else:
                occur[c] = 1

        for c in t:
            if c in occur:
                if occur[c] == 1:
                    del occur[c]
                else:
                    occur[c] -= 1
            else:
                return False

        if not occur:
            return True
        else:
            return False
        
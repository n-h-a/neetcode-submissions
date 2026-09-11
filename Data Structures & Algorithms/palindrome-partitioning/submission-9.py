class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome(x, l, r):
            while l < r:
                if x[l] != x[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
# GOAL
# ========
# Given a string s, return a list of all possible lists of 
# palindromic substrings.

# OBSERVATIONS
# ========
# Each element can only be used once in the result.

# Look at a letter
#   If i happens to be past the end, then we want to add a copy of l.
#   Decide whether to add it to last string in list or cut it.
#   
#   However, if the last string is not a palindrome, we can't cut.
# 
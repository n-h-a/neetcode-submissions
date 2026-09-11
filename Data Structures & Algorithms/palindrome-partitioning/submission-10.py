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
# For each index,
#   If the index is past last, then add partition to res.
#   Consider all possible substrings that could come from it.
#       If the substring is a palindrome,
#           Add it to partition.
#           Call dfs on next position after it.
#           Pop it from the partition.
# Call dfs on 0 and return res.
# TC: O(N * 2^N), SC: O(N)
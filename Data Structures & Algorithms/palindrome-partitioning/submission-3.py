class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, l = [], [s[0]]
        palindromes = {"", s[0]}

        def dfs(i):
            nonlocal l

            if i >= len(s):
                if l[-1] in palindromes:
                    res.append(l.copy())
                return

            if l[-1] in palindromes:
                l.append(s[i])
                palindromes.add(s[i])
                dfs(i + 1)
                l.pop()

            if l[-1][0] == s[i] and l[-1][1:] in palindromes:
                palindromes.add(l[-1] + s[i])

            l[-1] += s[i]
            dfs(i + 1)
            l[-1] = l[-1][:-1]

        dfs(1)
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
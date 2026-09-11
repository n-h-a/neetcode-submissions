class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, stack = [], [[s[0]]]
        palindromes = {"", s[0]}

        def dfs(i):
            nonlocal stack

            if i >= len(s):
                if "".join(stack[-1]) in palindromes:
                    res.append(["".join(x) for x in stack])
                return

            if "".join(stack[-1]) in palindromes:
                stack.append([s[i]])
                palindromes.add(s[i])
                dfs(i + 1)
                stack.pop()

            stack[-1].append(s[i])
            if stack[-1][0] == stack[-1][-1] and "".join(stack[-1][1:-1]) in palindromes:
                palindromes.add("".join(stack[-1]))

            dfs(i + 1)
            stack[-1].pop()

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
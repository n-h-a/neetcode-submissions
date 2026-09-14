class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if digits == "":
            return []

        res = []
        combo = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(combo))
                return

            digit = digits[i]
            for letter in letters[digit]:
                combo.append(letter)
                backtrack(i + 1)
                combo.pop()

        backtrack(0)
        return res

# GOAL
# ========
# Given a digit, return a list of all possible letter
# combinations that could represent it.

# IDEA
# ========
# Use backtracking. For each digit, and for each letter
# it maps to, create a path from that point.
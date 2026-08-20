class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            digit = ""
            while s[i] != "#":
                digit += s[i]
                i += 1
            digit = int(digit)
            i += 1

            word = ""
            for j in range(digit):
                word = word + s[i + j]
            res.append(word)
            i += digit

        return res

                



# GOAL
# ========
# Encode a list of strings --> string. 
# Then decode string --> list of strings.

# OBSERVATIONS
# ========
# * Need this to work on every possible character.
# * Length of string matters.

# IDEA
# ========
# * Before every string, we could have a number that denotes length.
#       Problem: Some numbers have multiple digits.
# * After every number, we could have a symbol that denotes end of number.

# PSEUDOCODE
# ========
# Encode
#   Add length + "#" + string to resulting string.
# Decode
#   While not at end of string,
#       Get length up until #
#       Grab word
#       Increment i by len of string

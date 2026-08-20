class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t == "+":
                operands.append(operands.pop() + operands.pop())
            elif t == "-":
                a, b = operands.pop(), operands.pop()
                operands.append(b - a)
            elif t == "*":
                operands.append(operands.pop() * operands.pop())
            elif t == "/":
                a, b = operands.pop(), operands.pop()
                operands.append(int(b / a))
            else:
                operands.append(int(t))

        return operands.pop()

# GOAL
# =========
# Return an integer that represents the evaluation
# of the expression.

# BRUTE FORCE
# =========
# While more than one token exists,
#   Loop through list,
#       If an operator is found,
#           Take the two operands before it and evalute.
#           Replace the two operands and operator from list
#               with computed value
#           Break
# TC: O(N^2)
# SC: O(N)

# IDEA
# ==========
# Why is brute force suboptimal?
#   It repeatedly scans the list over and over.
#   Same elements are scanned multiple times.
# Use a stack for operands.

# PSEUDOCODE
# ==========
# Loop through list,
#   If element is operand, 
#       Add it to operand stack.
#   If element is operator,
#       Pop off the two stack twice.
#       Compute and add result to operand stack.
# TC: O(N)
# SC: O(N)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        

# GOAL
# ==========
# Design a min stack that where each method is O(1).

# BRUTE FORCE
# ==========
# To find min, look through all elements in stack,
# push: Append it to stack.
# pop: Remove top element from stack.
# top: Return last element of stack.
# getMin: Create temp list, pop all elements from the stack and track
#   smallest value. Push all elements back. Return smallest value.'
# TC: O(N)
# SC: O(N)

# IDEA
# ==========
# Use another prefix stack to keep track of the minimum.
# push: Append it to stack. Compare to current min. 
#   If <, append to prefix stack.
#   Otherwise, append top of prefix stack to prefix stack.
# pop: Remove top element from stack. Remove top element from prefix stack.
# top: Return last element of stack.
# getMin: Return top element of prefix stack.
# TC: O(1)
# SC: O(N)


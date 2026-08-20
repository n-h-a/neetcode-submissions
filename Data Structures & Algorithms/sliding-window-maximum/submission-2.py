class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # Stores indices.
        l = r = 0

        while r < len(nums):
          # Pop smaller values from q.
          while q and nums[q[-1]] < nums[r]:
            q.pop()
          q.append(r)

          # If leftmost is no longer in bounds, remove from window.
          if l > q[0]:
            q.popleft()

          if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
          r += 1

        return output



# GOAL
# ==========
# Return a list that contains the max element in the window
# at each step.

# BRUTE FORCE
# ==========
# For each window,
#   Look for the max and append to result array.
# TC: O(N * k)

# OBSERVATIONS
# ===========
# Between each window, the max changes depending on the 
# start and end points. How?
#   The end point adds an element.
#   The start point removes an element.

# IDEA
# ==========
# Why is the brute force solution suboptimal?
#   We're scanning parts of windows we've already seen.
# Use a deque.
#   Property: Descending, so
#     max will always be leftmost.
#   If we see a value > prev values in window,
#     pop prev values from window.
#   If leftmost is no longer in bounds,
#     pop leftmost.
# Use indices in deque to track whether leftmost in bounds.
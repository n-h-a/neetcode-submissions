class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_p = 0
        min_b = prices[0]
        for p in prices:
            max_p = max(max_p, p - min_b)
            min_b = min(min_b, p)

        return max_p

# GOAL
# =========
# Return the maximum amount of profit you could make.

# BRUTE FORCE
# =========
# For each price p,
#   For each price q thereafter, 
#       Calculate profit p - q
#       Keep track of max profit
# TC: O(N^2)
# SC: O(1)

# IDEA
# =========
# Where is the extra work? What makes this inefficient?
#   Every time I'm evaluating a selling price, I'm making passes
#   through every buying price before it. When really, all I need
#   to do is just subtract the minimum buying price before it.
# The Idea
#   For each selling price,
#       Calculate and update max profit.
#       Update minimum.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total, res = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                res = i + 1
                total = 0
        return res

# GOAL
# =========
# Given two int arrays: gas and cost s.t.,
#   * gas: the amount of gas at the ith station
#   * cost: the amount of gas needed to travel from ith to (i+1)th station
# Return the starting index that can complete one CW circuit. -1 if DNE.

# BRUTE FORCE
# =========
# Try out every index and see if you can complete a circuit:
# TC: O(N^2), SC: O(1)
# Optimization: Find the nets. If anything is negative, skip it.

# IDEA
# =========
# Observation:
#   * You can move forward only if you have enough gas before leaving.
#   * Each gas-cost situation has a net impact.
#   * If sum(gas) < sum(cost), no solution possible. Otherwise, there always is.
# Keep track of current gas balance.
# Loop through indices with i.
#   Add net impact of the ith station to your total.
#   If the net impact of the ith station and cost makes your balance negative,
#       This is not a valid start. Move result index up and reset total to 0.
#   Otherwise, continue. It's a valid start.
# How do we know that a solution always exists though, especially for last station?
#   Because we checked with observation 3 first.
# TC: O(N)
# SC: O(1)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# GOAL
# ========
# Given int array and an int, k,
#   Return the k most frequent elements within the array.

# NOTE
# ========
# Answer is always unique.

# OBSERVATIONS
# ========
# At least O(N) since we have to keep track of every element + freq.

# BRUTE FORCE
# ========
# Count frequency of each number
# Sort based on frequency
# Select top k elements
# TC: O(NlogN)

# IDEA
# ========
# Initialize a table of size k s.t. the indices represent the count.
# 
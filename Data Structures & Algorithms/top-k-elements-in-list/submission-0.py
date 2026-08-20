class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

# GOAL
# ========
# Return the k most frequent elements within the array.

# OBSERVATIONS
# ========
# * Test cases guarantee unique answer.
# * Output can be in any order.

# BRUTE FORCE
# ========
# Create dictionary to keep track of frequencies.
# Sort the dictionary keys based on their values (frequencies).
# Return the k most frequent.
# TC: O(N log N)
# SC: O(N)

# IDEA
# ========
# Create a dictionary to keep track of counts for each nums.
# Create a bucket list of size N s.t. each index represents a frequency,
# and each value represents a list of nums with that frequency.
# Return the top k most elements.
# TC: O(N + N) == O(N)
# SC: O(N + N) == O(N)


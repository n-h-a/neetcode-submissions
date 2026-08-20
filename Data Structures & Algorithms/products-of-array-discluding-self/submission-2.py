class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1] * N
        suffix = [1] * N

        for i in range(1, N):
           prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        output = []
        for i in range(N):
            output.append(prefix[i] * suffix[i])

        return output
            


        



# GOAL
# ========
# Return an array, output, s.t. output[i] == product of all elements
# except nums[i].
# + Solve O(N) w/o divison

# BRUTE FORCE
# ========
# For each index, multiply all elements except itself.
# TC: O(N^2)

# IDEA
# ========
# Construct a prefix array and suffix array.
# For each position i, append prefix[i] * suffix[i]
# TC: O(N + N + N) -> O(N)
# SP: O(N + N) -> O(N)

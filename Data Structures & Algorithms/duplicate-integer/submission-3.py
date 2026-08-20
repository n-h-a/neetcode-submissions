class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



# GOAL
# ========
# Given array nums return true if there's a duplicate. 
# Otherwise, return false.

# BRUTE FORCE
# ========
# For each element in nums,
#   Loop through the rest of the list,
#       Check if any elements are dups. Return true if yes.
# Return false if no dups.
# TC: O(N^2)
# SC: O(1)

# IDEA
# =========
# Why is brute force suboptimal?
#   We're looping through each element over and over,
#       and do not have any memory of what we've seen before.
#   If there was a faster way to check whether an element
#       is in the list and has been seen, we avoid seeing that
#       element repeatedly.
# Use a hash set to store elements we've seen already.
#   Creation and retrieval is constant time.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occur = {}

        for num in nums:
            if num in occur:
                return True
            else:
                occur[num] = 1

        return False
        

# IDEA:
# Keep a dictionary of occurrences.
# Loop through entire array.
#   Check if element exists in dictionary. 
#       If yes, return True.
#       Otherwise, add to dictionary.
# If none found, return False.

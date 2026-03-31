class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> positions = new HashMap<>();
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (positions.containsKey(diff)) {
                result[0] = positions.get(diff);
                result[1] = i;
                return result;
            } else {
                positions.put(nums[i], i);
            }
        }

        return result;
        
    }
}

// GOAL: Given target, return indices i and j s.t. nums[i] + nums[j] == target.
//       Smallest index first.

// NOTES:
// * Smallest index first.
// * Exactly one pair of indices.

// OBSERVATIONS:
// * We have to go through every element in order to find this pair in the worst case.
//   --> O(N)

// BRUTE FORCE:
// For every element in the loop, loop through list and see if sum is target.
// O(N^2)

// PSEUDOCODE:
// Initialize hashmap.
// For every integer in nums,
//      Find difference between target and integer, diff.
//      Check if diff is inside hashmap.
//          If yes, then return integer and diff's index.
//          Otherwise, continue.
// Return {}.

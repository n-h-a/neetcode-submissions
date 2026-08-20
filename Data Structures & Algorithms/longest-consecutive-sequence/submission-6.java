class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int max_len = 0;
        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                max_len = Math.max(length, max_len);
            }
        }

        return max_len;
    }
}

// GOAL
// ========
// Return length of longest consecutive sequence.

// BRUTE FORCE
// ========
// VERSION 1
// For each number, build a consecutive sequence and update max length.
// TC: O(N^2)
// SC: O(1)
// VERSION 2
// Sort the list.
// Iterate through the list, updating max length.
// TC: O(N log N)
// SC: O(1)

// IDEA
// ========
// We just need to know if an element is in the list. -> Need fast look ups.
// Where is the extra work?
//      The extra work is checking each number. 
//          Ex: [1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5]
// We just need to look at the length of [1, 2, 3, 4, 5].

// PSEUDOCODE
// ========
// Construct a hash set for fast lookups.
// For every num in list,
//      If num does not start a sequence,
//          skip
//      Otherwise,
//          Use hashset to construct sequence and keep track of max length.


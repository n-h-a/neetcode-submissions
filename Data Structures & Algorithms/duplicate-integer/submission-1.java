class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> freq = new HashMap<>();

        for (int num : nums) {
            if (freq.containsKey(num)) return true;
            freq.put(num, true);
        }

        return false;
    }
}
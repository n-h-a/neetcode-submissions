class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();
        int[] res = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (indices.containsKey(diff)) {
                res[0] = indices.get(diff);
                res[1] = i;
                return res;
            } else {
                indices.put(nums[i], i);
            }
        }

        return res;
    }
}

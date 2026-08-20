class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1];

        for (int i = 0; i < nums.length + 1; i++) {
            freq[i] = new ArrayList<Integer>();
        }

        for (int num : nums) {
            int val = counts.getOrDefault(num, 0);
            counts.put(num, val + 1);
        }

        for (int num : counts.keySet()) {
            freq[counts.get(num)].add(num);
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int num : freq[i]) {
                res[index++] = num;
                if (index == k) {
                    return res;
                } 
            }
        }
        return res;
    }
}

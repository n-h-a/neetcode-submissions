class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<int[]> arr = new ArrayList<>();

        for (int n : nums) {
            if (count.containsKey(n)) {
                count.put(n, count.get(n) + 1);
            } else {
                count.put(n, 1);
            }
        }

        for (var entry : count.entrySet()) {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        }
        arr.sort((a, b) -> b[0] - a[0]);

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = arr.get(i)[1];
        }
        return res;
    }
}

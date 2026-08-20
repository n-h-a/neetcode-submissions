class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> freq = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (freq.containsKey(c)) {
                int val = freq.get(c);
                freq.put(c, val + 1);
            } else {
                freq.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (freq.containsKey(c)) {
                int val = freq.get(c);
                if (val == 1) {
                    freq.remove(c);
                } else {
                    freq.put(c, val - 1);
                }
            } else {
                return false;
            }
        }

        if (freq.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}

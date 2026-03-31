class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (freq.containsKey(c)) {
                Integer value = freq.get(c);
                freq.put(c, value + 1);
            } else {
                freq.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (freq.containsKey(c)) {
                Integer value = freq.get(c) - 1;
                if (value < 0) return false; 
                freq.put(c, value);
            } else {
                return false;
            }
        }

        return true;
    }
}

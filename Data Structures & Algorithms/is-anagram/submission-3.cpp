class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> freq;

        for (char c : s) {
            if (freq.count(c) == 0) {
                freq[c] = 1;
            } else {
                freq[c]++;
            }
        }

        for (char c : t) {
            if (freq.count(c) != 0) {
                freq[c]--;
                if (freq[c] < 0) return false;
            } else {
                return false;
            }
        }

        return true;
    }
};

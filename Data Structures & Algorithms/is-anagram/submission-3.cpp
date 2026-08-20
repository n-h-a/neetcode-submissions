class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        for (char c : s) {
            if (freq.contains(c)) {
                freq[c] += 1;
            } else {
                freq[c] = 1;
            }
        }

        for (char c : t) {
            if (freq.contains(c)) {
                if (freq[c] == 1) {
                    freq.erase(c);
                } else {
                    freq[c] -= 1;
                }
            } else {
                return false;
            }
        }

        if (freq.empty()) {
            return true;
        } else {
            return false;
        }
    }
};

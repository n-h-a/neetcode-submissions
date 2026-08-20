class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;

        for (int num : nums) {
            if (freq.contains(num)) {
                return true;
            } else {
                freq[num] = 1;
            }
        }

        return false;
    }
};
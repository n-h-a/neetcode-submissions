class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> freq;

        for (int num : nums) {
            if (freq.count(num) == 1) {
                return true;
            }
            freq[num] = 1;
        }

        return false;
    }
};
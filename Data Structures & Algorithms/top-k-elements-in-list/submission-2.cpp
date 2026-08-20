class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        vector<vector<int>> freq(nums.size() + 1);

        for (int num : nums) {
            counts[num] = 1 + counts[num];
        }

        for (const auto& entry : counts) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> res;
        for (int i = freq.size() - 1; i > 0; i--) {
            for (int num : freq[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        
        return res;
    }
};

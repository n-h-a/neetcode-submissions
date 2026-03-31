class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> positions;

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (positions.count(diff) != 0) {
                return {positions[diff], i};
            } else {
                positions[nums[i]] = i;
            }
        }

        return {};
    }
};

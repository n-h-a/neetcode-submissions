class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (indices.contains(diff)) {
                return {indices[diff], i};
            } else {
                indices[nums[i]] = i;
            }
        }

        return {};
    }
};

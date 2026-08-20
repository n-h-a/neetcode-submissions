class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        vector<int> res(2);

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (indices.contains(diff)) {
                res[0] = indices[diff];
                res[1] = i;
                return res;
            } else {
                indices[nums[i]] = i;
            }
        }

        return res;
    }
};

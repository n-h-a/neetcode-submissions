class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int N = nums.size();
        vector<int> prefix(N, 1);
        vector<int> suffix(N, 1);

        for (int i = 1; i < N; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = N - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        vector<int> output(N);
        for (int i = 0; i < N; i++) {
            output[i] = prefix[i] * suffix[i];
        }
        return output;
    }
};

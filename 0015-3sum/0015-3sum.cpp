class Solution {
public:
    vector<vector<int>> result;

    void twoSum(vector<int>& nums, int target, int i, int j) {
        while (i < j) {
            int sum = nums[i] + nums[j];
            if (sum > target) {
                j--;
            } else if (sum < target) {
                i++;
            } else {
                result.push_back({-target, nums[i], nums[j]});
                while (i < j && nums[i] == nums[i + 1]) i++;
                while (i < j && nums[j] == nums[j - 1]) j--;
                i++;
                j--;
            }
        }
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        result.clear();
        if (n < 3) return {};

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;  // skip duplicate n1
            int n1 = nums[i];
            int target = -n1;
            twoSum(nums, target, i + 1, n - 1);
        }
        return result;
    }
};

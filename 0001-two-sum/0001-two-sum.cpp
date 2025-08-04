// --- BRUTE FORCE O(n^2)
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         int n = nums.size();
//         for (int i=0;i<n-1;i++){
//             for (int j=i+1;j<n;j++){
//                 if (nums[i]+nums[j]== target){
//                     return {i,j};
//                 }
//             }
//         }
//         return {};
//     }
// };

// better approach O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int> mp;
        for (int i=0;i<n;i++){
            int remainder = target - nums[i];
            if (mp.find(remainder) !=mp.end()){
                return {mp[remainder],i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};
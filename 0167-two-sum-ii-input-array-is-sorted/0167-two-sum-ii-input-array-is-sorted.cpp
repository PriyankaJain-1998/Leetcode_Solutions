class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i =0, j = numbers.size()-1;
        for (int k=0;k<numbers.size();k++){
            if (numbers[i]+numbers[j]<target){i+=1;}
            else if (numbers[i]+numbers[j]>target){j-=1;}
            else{ return {i+1, j+1};}
        }
        return {};
    }
};
class Solution {
public:
    bool isPalindrome(int x) {
        int x_size = std::to_string(x).length();
        if (x<0 || (x%10==0 && x!=0)){ return false;}
        int reversed = 0;
        while (x>reversed){
            reversed = reversed *10 +x %10;
            x/=10;
        }
        return x==reversed || x==reversed/10;
        // if (x>0){
        //     x =std::to_string(x);
        //     int left = 0
        //     int right = x_size-1
        //     if (left<right){
        //         if (x[left]!=x[right]){
        //             return false
        //         }
        //     }
        //     else{
        //         left +=1
        //         right -=1
        //     }
        // }
    }
};
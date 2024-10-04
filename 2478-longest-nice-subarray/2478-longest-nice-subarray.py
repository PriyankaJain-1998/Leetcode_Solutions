class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start, max_nice = 0,0
        for i in range(len(nums)):
            temp = start 
            while temp<i:
                if nums[i] & nums[temp]!=0:
                    start = temp+1
                temp+=1
            max_nice = max(max_nice, i-start+1)

        return max_nice
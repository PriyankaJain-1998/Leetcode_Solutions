class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # ans,count = 0,0
        # for i in arr1:
        #     for j in arr2:
        #         if abs(i-j)<=d:
        #             count+=1
        #     if count==0: ans+=1
        #     count = 0
        # return ans
        arr2.sort()
        res = 0
        for i in arr1:
            start, end = 0, len(arr2)-1
            while(start<=end):
                mid = (start + (end-start)//2)
                if abs(i-arr2[mid])<=d: break 
                elif i < arr2[mid]: end = mid-1
                else : start = mid+1
            else: 
                res+=1

        return res
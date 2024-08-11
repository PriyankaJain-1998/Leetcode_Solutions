class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # arr1 = sorted(arr1)
        # arr2 = sorted(arr2)
        ans,count = 0,0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count+=1
            if count==0: ans+=1
            count = 0

        return ans
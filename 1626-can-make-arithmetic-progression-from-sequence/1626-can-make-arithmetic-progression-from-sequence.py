class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = abs(arr[0]-arr[1])
        for i in range(2,len(arr)):
            # print(arr, diff,arr[i]-arr[i-1] )
            if abs(arr[i]-arr[i-1])!=diff: return False
        return True
class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start<=end:
            mid = start+(end-start)//2
            temp = int(mid*(mid+1)/2)
            if temp == n: return mid
            elif temp < n: start = mid+1
            else: end = mid-1
        return end
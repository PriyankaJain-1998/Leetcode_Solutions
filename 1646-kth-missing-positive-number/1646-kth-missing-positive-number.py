class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # ideal_arr = list(range(1,1001))
        # return list(set(ideal_arr)^set(arr))[k-1]

        start = 0
        end = len(arr)-1
        while start <= end:
            mid = start+(end-start)//2
            if arr[mid]-mid-1 < k:
                start = mid+1
            else:
                end = mid-1
        return start+k
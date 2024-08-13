class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def carShip(mid):
            ships, currCap = 1, mid
            for i in weights:
                if currCap - i <0:
                    ships+=1
                    currCap = mid
                currCap-=i
            return ships<=days

        while (l<=r):
            mid = (l+r)//2
            if carShip(mid):
                res = min(res,mid)
                r = mid-1
            else:
                l = mid+1

        return res
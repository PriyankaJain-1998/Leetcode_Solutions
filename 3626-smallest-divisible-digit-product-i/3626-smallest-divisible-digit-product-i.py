class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,100+1):
            if i<10:
                if ((i%10)%t)==0: return i
            elif ((i%10)*(i//10))%t == 0: return i 
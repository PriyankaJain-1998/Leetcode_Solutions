class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==1: return True
        for i in range(0, 32):
            if (pow(2,i)==n): return True 
            if (pow(2,i)>n): return False
        return False        
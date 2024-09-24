class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        setBits = 0
    
        while (a > 0) :
            setBits += a & 1
            a >>= 1
        
        return setBits 
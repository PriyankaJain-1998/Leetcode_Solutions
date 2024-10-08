class Solution:
    def concatenatedBinary(self, n: int) -> int:
        d = ""
        M = 10**9 +7
        for i in range(n+1):
            d += str(bin(i)[2:])
        return int(d,2) % M
        
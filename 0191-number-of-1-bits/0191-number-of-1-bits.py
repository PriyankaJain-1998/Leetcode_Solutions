class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(str(bin(n)))['1']
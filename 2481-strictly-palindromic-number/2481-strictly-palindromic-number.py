class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base(b, num):
            digits = []
            while num:
                digits.append(int(num % b))
                num //= b
            return digits

        for b in range(2,n-2):
            d = base(b, n)
            if d != d[::-1]: 
                return False
                


            
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        # if n == 0:return [0]

        def base(b, num):
            digits = []
            while num:
                digits.append(int(num % b))
                num //= b
            return digits

        for b in range(2,n-2):
            d = base(b, n)
            print(d)
            if d != d[::-1]: 
                return False

        # return True
                


            
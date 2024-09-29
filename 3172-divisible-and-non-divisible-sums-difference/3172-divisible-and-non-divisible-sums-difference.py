class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = [],[]
        for i in range(1,n+1):
            print(i)
            if i%m==0: num2.append(i)
            else: num1.append(i)
        print(num1, num2)
        return sum(num1)-sum(num2)
        
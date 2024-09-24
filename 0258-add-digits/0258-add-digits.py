class Solution:
    def addDigits(self, num: int) -> int:
        # if num<10: return num
        while (num>9):
            sum = 0
            while num:
                sum += num%10
                num = num//10
            num = sum
        return num

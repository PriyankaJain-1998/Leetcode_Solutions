class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum(list(map(int, list(str(x)))))
        if x%digit_sum == 0: return digit_sum
        else: return -1
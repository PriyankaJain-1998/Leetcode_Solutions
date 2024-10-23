class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        output, p = 0, 'I'
        for i in s[::-1]:
            # output += roman[i]
            output, p = output - roman[i] if roman[i] < roman[p] else output + roman[i], i
        return output

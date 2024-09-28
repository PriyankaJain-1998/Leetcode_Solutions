class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        indices = [i for i, digit_ in enumerate(number) if digit_ == digit]
        output = 0
        number_list = list(number)
        for index in indices: 
            number_list[index] = "X"
            temp = int("".join(number_list).replace("X",""))
            if temp > output: output = temp
            number_list = list(number)
        return str(output)
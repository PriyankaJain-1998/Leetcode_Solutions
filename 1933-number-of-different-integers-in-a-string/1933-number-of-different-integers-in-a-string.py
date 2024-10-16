class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        string, sub_arr = "", []
        for i in range(len(word)):
            if not word[i].isdigit():
                word = word.replace(word[i]," ")
        return len(set(list(map(int, word.split()))))
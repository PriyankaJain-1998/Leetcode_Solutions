class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        for sen in sentences:
            sen = len(sen.split())
            if sen>output: output = sen

        return output
        
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for word in range (len(sentence)):
            if searchWord in sentence[word]:
                if searchWord == sentence[word][0:len(searchWord)]:
                    return word+1

        return -1

        
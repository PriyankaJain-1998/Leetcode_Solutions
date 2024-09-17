class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # return sequence.count(word)
        i = 0
        while word*(i+1) in sequence:
            i+=1
        return i
        
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        output = 0
        if s in words: output += words.count(s)
        for i in range(len(s)):
            if s[0:i] in words: output +=words.count(s[0:i])
        return output
        
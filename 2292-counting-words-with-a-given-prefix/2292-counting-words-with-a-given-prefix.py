class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output = 0
        for word in words:
            if pref==word[0:len(pref)]:
                output+=1
        return output
        
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(0,len(s)):
            temp = s[i]
            s[i] = temp[::-1]

        return " ".join(s)
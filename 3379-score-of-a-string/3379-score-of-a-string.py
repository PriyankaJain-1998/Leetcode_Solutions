class Solution:
    def scoreOfString(self, s: str) -> int:
        s = list(s)
        output = 0
        for i in range(len(s)-1, 0, -1):
            # print(ord(s[i]), " ", ord(s[i-1]), " ",abs(ord(s[i])-ord(s[i-1])))
            output += abs(ord(s[i])-ord(s[i-1]))

        return output
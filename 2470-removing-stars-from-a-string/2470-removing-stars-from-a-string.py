class Solution:
    def removeStars(self, s: str) -> str:
        for i in s:
            if i == "*":
                index = s.index("*")
                s = s[:index-1]+s[index+1:]

        return s
                
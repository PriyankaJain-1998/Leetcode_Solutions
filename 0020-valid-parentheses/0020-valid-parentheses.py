class Solution:
    def isValid(self, s: str) -> bool:
        while len(s)>0:
            l = len(s)
            s = s.replace("()",'').replace("[]",'').replace("{}",'')
            if len(s)==l: return False
        return True
        
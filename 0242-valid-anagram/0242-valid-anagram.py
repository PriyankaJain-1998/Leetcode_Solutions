class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s)==set(t) and len(s)==len(t): 
            for i in s:
                if s.count(i)!=t.count(i): return False
            return True
        return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = "".join(re.sub(r'[^\w\s]','',s).lower().split())
        if "_" in s: 
            s = s.replace("_","")
            
        if s == s[::-1]: return True


        
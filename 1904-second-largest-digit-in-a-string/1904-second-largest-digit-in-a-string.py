class Solution:
    def secondHighest(self, s: str) -> int:
        s= sorted(set([int(i) for i in s if i.isdigit()]))
        if len(s)>1:return s[-2]
        else: return -1

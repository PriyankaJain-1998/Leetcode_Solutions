class Solution:
    def maxPower(self, s: str) -> int:
        ans,c = 1,1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
                ans=max(c,ans)
            else: c=1
        return ans
        
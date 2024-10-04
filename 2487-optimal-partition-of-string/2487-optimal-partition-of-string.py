class Solution:
    def partitionString(self, s: str) -> int:
        ans, res = "", []
        for ch in s:
            if ch in ans:
                res.append(ans)
                ans = ""
                ans+=ch
            else:
                ans+=ch
        return len(res)+1
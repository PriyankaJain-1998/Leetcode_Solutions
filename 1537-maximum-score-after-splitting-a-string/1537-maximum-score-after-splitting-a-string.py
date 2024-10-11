class Solution:
    def maxScore(self, s: str) -> int:
        max_score = left = 0
        right = s.count("1")
        for i in range(len(s)-1):
            left +=s[i] == '0'
            right -=s[i]=='1'
            max_score = max(max_score, left+right)

        return max_score
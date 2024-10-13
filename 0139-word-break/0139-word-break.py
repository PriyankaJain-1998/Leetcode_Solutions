class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # stack = ""
        # wordDict = set(wordDict)
        # count = 0
        # for i in range(len(s)):
        #     stack+=s[i]
            
        #     if stack in wordDict:
        #         print("in")
        #         count+=1
        #         stack = ""
        #     if count == len(wordDict): return True
        # return False

        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        max_len = max(map(len, wordDict))
        for i in range(1,n+1):
            for j in range(i-1,max(i-max_len-1,-1),-1):
                if dp[j] and s[j:i]in wordDict:
                    dp[i]=True
                    break
        return dp[n]
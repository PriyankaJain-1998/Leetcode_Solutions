class Solution:
    def fib(self, n: int) -> int:
        # dp = [-1]*(n+1)
        # if (n==0 or n==1): 
        #     return n
        # if (dp[n]!=-1): return dp[n]
        # dp[n] = self.fib(n-1)+self.fib(n-2)
        # return dp[n]
        if n==0 or n==1: return n
        dp = [-1]*(n+1)
        dp[1]= 1
        dp[0]= 0
        
        
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
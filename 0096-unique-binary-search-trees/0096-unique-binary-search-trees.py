class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Follow the below steps to Implement the idea:

            Create an array DP of size n+1
            DP[0] = 1 and DP[1] = 1.
            Run for loop from i = 2 to i <= n
            Run a loop from j = 1 to j <= i
            DP[i] = DP[i] + (DP[i – j] * DP[j – 1])
            Return DP[n]
        '''
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] = dp[i] + (dp[i-j]*dp[j-1])
        return dp[n]
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res= {}

        def dp(x, steps, res):
            if x == 1:
                return steps
            
            if x%2==0:
                x = x//2
                steps+=1

            else:
                x = 3*x+1
                steps+=1
                
            if x in res:
                return steps + res[x]
            
            return dp(x,steps,res)
        

        for i in range(lo,hi+1):
            res[i]=dp(i,0,res)

        res = sorted(res.items(), key=lambda kv: kv[1])[k-1][0]
        return res
            

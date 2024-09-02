class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        # while k>=sum_chalk: k-=sum_chalk
        k = k%sum_chalk
        for i in range(len(chalk)):
            k = k-chalk[i]
            if k<0: return i
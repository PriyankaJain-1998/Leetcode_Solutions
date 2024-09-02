class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # student = -1
        # while (k>0):
        #     for i in chalk:
        #         k = k-i
        #         student +=1
        #         print(k,student)
        #         if k<i or k<0: 
        #             if student+1 == len(chalk): return 0
        #             return student+1
        #         if student==len(chalk)-1 and k>=0: student=-1
        # if student==-1: student = 0
        # return student

        
        sum_chalk = sum(chalk)
        # while k>=sum_chalk: k-=sum_chalk
        k = k%sum_chalk
        for i in range(len(chalk)):
            k = k-chalk[i]
            if k<0: return i
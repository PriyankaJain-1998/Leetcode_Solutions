class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # difficulty, worker, profit =sorted(difficulty), sorted(worker), sorted(profit)
        # print(difficulty, worker, profit)
        # max_profit=0
        # for i in worker:
        #     sublist = [element for element in difficulty if element <= i]
            
        #     if len(sublist)>0: 
        #         print(sublist, max(profit[:len(sublist)]))
        #         # index = difficulty.index(i)
        #         # diff_ = difficulty[:index]
        #         # print(diff_,profit[:index])
        #         max_profit += max(profit[:len(sublist)])
        # print(max_profit)
        # return max_profit

        jobs = sorted(zip(difficulty,profit))
        print(jobs)
        worker.sort()
        max_profit, best, i, n = 0,0,0,len(jobs)
        for ability in worker:
            while i<n and jobs[i][0]<=ability:
                best=max(best,jobs[i][1])
                i+=1
            max_profit+=best
        return max_profit

            


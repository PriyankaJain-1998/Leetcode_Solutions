class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # ans = set()
        # n = len(nums)
        # for i in range(0,n-3):
        #     for j in range(i+1,n-2):
        #         for k in range(j+1,n-1):
        #             for z in range(k+1,n):
        #                 if nums[z]+nums[k]+nums[j]+nums[i]==target:
        #                     ans.add(tuple(sorted(([nums[z],nums[k],nums[j],nums[i]]))))

        # print(ans)
        # res=[]
        # for i in ans: res+=list(i),
        # print(res)
        # return res

        output = []
        n = len(nums)
        nums = sorted(nums)
        for p in range(0,n-3):
            ## skipping duplicates 
            if p > 0 and nums[p] == nums[p - 1]:continue
            for k in range(p+1, n-2):
                if k > p + 1 and nums[k] == nums[k - 1]:continue
                i,j = k+1, n-1
                while(i<j):
                    ans = nums[p]+nums[k]+nums[i]+nums[j]
                    
                    if ans<target: i+=1
                    elif ans>target: j-=1
                    else: 
                        output.append([nums[p],nums[k],nums[i],nums[j]])
                        while(i<j and nums[i]==nums[i+1]): i+=1
                        while(i<j and nums[j]==nums[j-1]): j-=1
                        
                        i+=1
                        j-=1
        print(output)
        return output
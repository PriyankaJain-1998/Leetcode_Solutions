class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i,j = 0,len(nums)-1
        # while(i<j):
        #     if nums[i]>nums[j]:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         print(i,j,nums)
        #         i+=1
        #         j-=1
                
        #     else:
        #         i+=1
        #         j-=1

        ### -- O(n^2)
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]

        
        ### -- TLE
        # n = len(nums)
        # i,j,k = 0,0,n-1
        # while(j<=k):
        #     if (nums[j]==1): j+=1
        #     elif nums[j]==2: nums[j], nums[k] = nums[k], nums[j]
        #     else:
        #         nums[j], nums[i] = nums[i], nums[j] 
        #         i+=1
        #         j+=1

        ### 
        i,j,k = 0,0,0
        for n in nums:
            if n==0: i+=1
            elif n==1: j+=1
            else: k+=1
        for p in range(len(nums)):
            if i>0:
                nums[p]=0
                i-=1
            elif j>0:
                nums[p]=1
                j-=1
            else:
                nums[p]=2
                k-=1
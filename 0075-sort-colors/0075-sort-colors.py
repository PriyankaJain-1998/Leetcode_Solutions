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

        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]

        
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        boundary, count = nums[0],0
        for i in range(1,len(nums)):
            boundary += nums[i]
            if boundary==0:count+=1
        return count 
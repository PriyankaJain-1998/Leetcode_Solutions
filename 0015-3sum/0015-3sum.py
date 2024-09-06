class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range (len(nums)-2):
            if i>0 and nums[i]==nums[i]-1: 
                continue

            left , right = i+1, len(nums)-1
            while left<right:
                sumtotal = nums[i] + nums[left] + nums[right]

                if sumtotal<0: left = left+1
                elif sumtotal>0: right = right -1 
                else: 
                    res.add((nums[i],nums[left],nums[right]))
                    while left<right and nums[left]==nums[left+1]: left = left+1
                    while left<right and nums[right]==nums[right-1]: right = right-1

                    left = left+1 
                    right = right-1
        return res
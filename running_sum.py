class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]  
        return nums

nums = [1,2,3,4]
S = Solution()
final_sum = S.runningSum(nums)
print(final_sum)

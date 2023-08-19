#
# @lc app=leetcode id=2670 lang=python
#
# [2670] Find the Distinct Difference Array
#

# @lc code=start
class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums.sort()
        # return [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        output = []
        for i in range (0, len(nums)):
            l1 = nums[:i+1]
            l2 = nums[i+1:len(nums)+1]
            output.append(len(set(l1))- len(set(l2)))
        return output 
    
        
# @lc code=end


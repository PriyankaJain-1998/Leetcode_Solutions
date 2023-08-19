#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if nums[j] > nums[j + 1]:
                    swapped = True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            
            if not swapped:
                return
        
# @lc code=end


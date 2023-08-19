#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]== target):
                    final.append(i)
                    final.append(j)
        return final
# @lc code=end


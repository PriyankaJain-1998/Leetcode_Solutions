#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in nums:
            if i%2 == 0:
                output.insert(0,i)
            else:
                output.append(i)
        return output
        
# @lc code=end


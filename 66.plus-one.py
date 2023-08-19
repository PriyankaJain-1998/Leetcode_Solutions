#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        final_dg = []
        digits = map(str, digits)
        digits = str(int([''.join(digits[0 : ])][0]) + 1 )
        digits = map(int, str(digits))
        return digits
# @lc code=end


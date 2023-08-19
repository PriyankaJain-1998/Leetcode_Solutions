#
# @lc app=leetcode id=2525 lang=python
#
# [2525] Categorize Box According to Criteria
#

# @lc code=start
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        f = 10**4
        volumn = length*width*height
        if ((length>=f or width>=f or height>=f) and mass>100):
            return "Bulky", "Heavy"
        if (mass > 100):
            
# @lc code=end


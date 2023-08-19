#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start

from collections import Counter 
import numpy as np 

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while(n!=0):
            n = n&(n-1)
            count+=1
        return(count)
# @lc code=end


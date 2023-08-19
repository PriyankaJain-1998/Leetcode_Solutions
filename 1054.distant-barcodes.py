#
# @lc app=leetcode id=1054 lang=python
#
# [1054] Distant Barcodes
#

# @lc code=start

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        dup_index = 0
        for i in range(-1, len(barcodes)):
            if(barcodes[i+1]==barcodes[i+2]):
                dup_index += i+1
            else:
                barcodes[i+1], barcodes[dup_index] = barcodes[dup_index],barcodes[i+1] 
                
# @lc code=end


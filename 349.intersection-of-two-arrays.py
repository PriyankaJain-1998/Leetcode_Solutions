#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        final_list = list()
        for i in set(nums1):
            if i in set(nums2):
                final_list.append(i)
        return final_list
# @lc code=end


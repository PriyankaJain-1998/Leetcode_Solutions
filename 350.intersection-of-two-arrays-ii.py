#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#
from collections import Counter
# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_cont = Counter(nums1)
        nums2_cont = Counter(nums2)
        final_list = list()
        for i in nums1:
            if i in nums2:
                final = Counter(final_list)
                if ((nums1_cont[i] <= nums2_cont[i] and final[i]!=nums1_cont[i]) or i not in final_list):
                    final_list.append(i)

                elif ((nums1_cont[i] >= nums2_cont[i] and final[i]!=nums2_cont[i]) or i not in final_list):
                    final_list.append(i)
        return final_list
        
# @lc code=end


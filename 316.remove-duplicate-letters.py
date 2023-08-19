#
# @lc app=leetcode id=316 lang=python
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # unique_chr = []
        # for i in list(s):
        #     if i not in unique_chr:
        #         unique_chr.append(i)
        return "".join(sorted(set(s)))
        
# @lc code=end
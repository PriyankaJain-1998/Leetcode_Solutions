#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_count = Counter(ransomNote.lower())
        magazine_count = Counter(magazine.lower())

        for k,v in ransomNote_count.items():
            if k not in magazine_count or magazine_count[k] < v:
                return False
            
        return True


        
# @lc code=end


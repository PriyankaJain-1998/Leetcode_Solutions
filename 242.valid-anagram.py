#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_words = Counter(s)
        t_words = Counter(t)
        
        if set(s)==set(t) and len(s)==len(t):
            for i in set(s):
                if s_words[i] == t_words[i]:
                    continue
                else:
                    return False
            return True
        else: return False
        
# @lc code=end


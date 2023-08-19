#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_value = max(nums)

        count = 0
        for i in nums:
            print(i)
            if maximum_value >= i*2:
                count +=1
                continue
            # else:
            #     return -1
        
        if count == len(nums):
            return nums.index(maximum_value)
        else: return -1
        
# @lc code=end


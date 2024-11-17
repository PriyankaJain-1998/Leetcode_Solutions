class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ele = max(nums)
        for i in nums:
            if i == max_ele: pass
            elif i*2 > max_ele: 
                return -1
        
        return nums.index(max_ele)
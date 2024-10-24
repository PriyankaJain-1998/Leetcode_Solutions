class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        multiply = 1
        for i in nums:
            multiply = multiply*i
        if multiply>0: return 1
        else: return -1
        
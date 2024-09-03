class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for k,v in nums.items():
            if v == 1: return k
        
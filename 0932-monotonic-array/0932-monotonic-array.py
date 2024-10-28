class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_in, nums_de = sorted(nums), sorted(nums,reverse=True)
        if nums==nums_in or nums==nums_de: return True
        else: return False
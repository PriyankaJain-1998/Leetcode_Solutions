class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2: return 0
        nums = sorted(nums)
        min_diff = min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
        return min_diff
        
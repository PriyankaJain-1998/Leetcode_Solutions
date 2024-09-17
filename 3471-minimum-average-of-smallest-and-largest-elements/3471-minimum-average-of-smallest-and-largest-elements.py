class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        averages = []
        for i in range(len(nums)//2):
            averages.append((nums[0]+nums[-1])/2)
            nums.remove(nums[0])
            nums.remove(nums[-1])
        return min(averages)
        
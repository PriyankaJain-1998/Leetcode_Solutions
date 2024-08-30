class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # if sum(nums[1:])==nums[0]: return nums[0]
        for i in range(len(nums)):
            # print(nums[:i],nums[i+1:])
            if sum(nums[:i])==sum(nums[i+1:]): return i

        return -1
        
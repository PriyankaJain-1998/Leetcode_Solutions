class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # if nums==sorted(nums): return sum(nums)
        # if nums==sorted(nums, reverse=True): return max(nums)

        sum_, final = nums[0], nums[0]
        for i in range (1, len(nums)):
            if nums[i]>nums[i-1]: 
                sum_+=nums[i]
            else: 
                sum_= nums[i]

            final = max(final,sum_)

        return final

        return sum_
        
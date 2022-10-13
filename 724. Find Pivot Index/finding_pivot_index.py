class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i in range(0,len(nums)):
            if (left_sum == (total-nums[i]-left_sum)):
                return i
            left_sum +=nums[i]
        return -1

nums = [1,7,3,6,5,6]
S = Solution()
final_sum = S.pivotIndex(nums)
print("PIVOT INDEX : ", final_sum)

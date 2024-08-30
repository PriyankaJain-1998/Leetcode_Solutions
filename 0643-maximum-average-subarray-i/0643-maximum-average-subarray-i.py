class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #-------- causes TLE
        # avg = sum(num[:k])
        # for i in range(k, len(nums)):
        #     n_ = nums[i:i+k]
        #     if len(n_)==k:
        #         avg_subarray = sum(n_)
        #         if avg<avg_subarray: avg = avg_subarray
        # return avg  
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k

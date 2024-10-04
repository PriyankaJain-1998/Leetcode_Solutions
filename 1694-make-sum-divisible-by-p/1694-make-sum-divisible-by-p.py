class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums)%p
        if remainder==0: return 0
        n, minlength, prefixsum, prefixsums = len(nums), len(nums), 0, {0:-1}
        for i in range(len(nums)):
            prefixsum = (prefixsum+nums[i])%p
            target = (prefixsum-remainder+p)%p

            if target in prefixsums:
                minlength = min(minlength, i-prefixsums[target])
            prefixsums[prefixsum]=i

        return minlength if minlength<n else -1        
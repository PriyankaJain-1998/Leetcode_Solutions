class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = consecutive = 0 
        for n in nums:
            consecutive = consecutive*n+n
            count = max(count, consecutive)
        return count
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i<j:
                    output +=1

        return output
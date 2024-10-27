class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums = Counter(nums)
        answer = 0 
        for k,v in nums.items():
            if v == 1: answer+=k
        return answer
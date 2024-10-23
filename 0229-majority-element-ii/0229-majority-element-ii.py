class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        nums = Counter(nums)
        ans = []
        for k,v in nums.items():
            if v>n: ans.append(k)
        return ans
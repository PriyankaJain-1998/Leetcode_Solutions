class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for i in nums:
            n2 = i+diff
            if n2 in nums and n2+diff in nums: ans +=1
        return ans

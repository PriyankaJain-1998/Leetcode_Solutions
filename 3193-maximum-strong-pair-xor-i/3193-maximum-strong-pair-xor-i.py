class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # xor_output = 0
        # for x in nums:
        #     for y in nums: 
        #         if x<=y and abs(x-y)<=min(x,y):
        #             xor_output = max(xor_output, x^y)

        return max(x^y for x in nums for y in nums if x<=y and abs(x-y)<=min(x,y))
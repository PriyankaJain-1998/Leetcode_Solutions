class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # strong_pairs = [[x, x] for x in nums]
        
        # strong_pairs = [(x,y) for x in nums for y in nums if x<=y and abs(x-y)<=min(x,y)]
        # print(strong_pairs, len(strong_pairs))
        xor_output = 0
        for x in nums:
            for y in nums: 
                if x<=y and abs(x-y)<=min(x,y):
                    xor_output = max(xor_output, x^y)

        return xor_output
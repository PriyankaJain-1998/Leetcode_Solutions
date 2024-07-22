class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1,-1]
        else: 
            indices= [ind for ind,ele in enumerate(nums) if ele==target]
            print(indices)
            if len(indices)==1: indices=indices*2
            elif len(indices)>2: indices = [indices[0], indices[len(indices)-1]]
            return indices
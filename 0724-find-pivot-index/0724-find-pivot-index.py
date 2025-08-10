class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if sum(nums[:i])==sum(nums[i+1:]): return i
        # return -1

        total, left = sum(nums),0
        for i in range(len(nums)):
            right = total-left-nums[i]
            if left==right: return i 
            left +=nums[i]
        return -1
        
        
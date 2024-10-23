class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
    
        if nums==[0] or set(nums)=={0}: return 0
        ans = 0
        def zeroarr(nums, ans):
            minval = min(nums)
            if minval == 0: minval = min(list(filter(lambda num: num != 0, nums)))
            nums = [x - minval if x != 0 else 0 for x in nums]
            ans[0] +=1
            if set(nums)!={0}: zeroarr(nums, ans)
            return ans[0]

        a = zeroarr(nums, ans=[0])
        return a
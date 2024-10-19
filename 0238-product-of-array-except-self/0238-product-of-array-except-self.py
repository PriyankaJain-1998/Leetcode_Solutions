class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # -------- tle
        # ans = [-1]*(len(nums))
        # output = []
        # for i in range(len(nums)):
        #     pre, post = nums[:i], nums[i:]
        #     del post[0]

        #     new_nums = pre+post
        #     output.append(math.prod(new_nums))
        # return output   

        n = len(nums)
        prefix, suffix = [1]*n, [1]*n 

        for i in range(1,n): prefix[i]=prefix[i-1]*nums[i-1] 
        for i in range(n-2,-1,-1): suffix[i] = suffix[i+1]*nums[i+1]
        return [prefix[i]*suffix[i] for i in range(n)]      
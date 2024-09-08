class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## ----------- Time limit Exceeded ----------------
        # for j in range (k):
        #     last_ele = nums[len(nums)-1]
        #     for i in range (len(nums)-1,0, -1):
        #         nums[i] = nums[i-1]
        #         print(i)
        #     nums[0] = last_ele

        ## ----------------------------
        n = len(nums)
        k = k%n
        print(k)
        nums[:] = nums[n-k:] + nums[:n-k]
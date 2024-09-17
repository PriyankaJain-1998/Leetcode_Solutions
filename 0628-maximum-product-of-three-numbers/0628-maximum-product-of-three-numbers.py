class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        triplet_sum = -inf
        for i in range(len(nums)-1, -1, -1):
            temp = nums[i]*nums[i-1]*nums[i-2]
            if temp>triplet_sum:
                triplet_sum = temp
        print(triplet_sum)
        return triplet_sum
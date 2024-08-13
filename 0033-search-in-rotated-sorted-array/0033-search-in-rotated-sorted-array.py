class Solution:
    # def getpivot(self, nums):
    #     start, end = 0, len(nums)-1
    #     while start<end:
    #         mid = int(start + (end-start)/2)
    #         if nums[mid]>=nums[0]:
    #             start = mid+1
    #         else: end = mid-1
    #     return start  

    # def binarysearch(self, nums, start, end, key):
    #     s = start
    #     e = end
        
    #     while s <= e:
    #         mid = int(s +(e-s)/2)
    #         if nums[mid]==key:
    #             return mid
    #         elif key>nums[mid]:
    #             s = mid +1
    #         else: e = mid -2

    #     return -1

    def search(self, nums: List[int], target: int) -> int:

        ## direct way 
        if target in nums: return nums.index(target)
        else: return -1

        ## using binary search 
        # pivot = self.getpivot(nums)
        # if (target>=nums[pivot] and target<=nums[len(nums)-1]):
        #     return self.binarysearch(nums, pivot, len(nums)-1, target)
        # else: 
        #     return self.binarysearch(nums,0, pivot-1, target)


        
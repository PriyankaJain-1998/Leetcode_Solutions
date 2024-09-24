class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start, end = 0,0

        while start<len(nums) and end<len(nums):
        #     j = i
            if (end + 1) < len(nums) and nums[end + 1] == nums[end] + 1:
                end+=1
            else:
                if nums[start]==nums[end]:
                    ans.append(str(nums[start]))
                    start += 1
                    end +=1
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[end]))
                    end +=1
                    start = end

        return ans
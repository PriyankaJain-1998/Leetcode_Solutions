class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # sorted_nums = sorted(nums)
        # ans = 0
        # for i in range(0,len(nums)):
        #     j = i+2
        #     while j<=len(nums):
        #         subsequence=sorted_nums[i:j]
        #         if max(subsequence)-min(subsequence)==1:
        #             ans = max(ans,len(subsequence))
        #         j +=1
        # return ans

        if not nums:return 0
        freq = Counter(nums)
        max_length = 0
        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])

        return max_length
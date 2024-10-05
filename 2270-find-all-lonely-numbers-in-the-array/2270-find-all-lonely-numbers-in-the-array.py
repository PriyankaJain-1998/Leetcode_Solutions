class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in nums:
        #     if nums.count(i)==1 and (i+1 not in nums) and (i-1 not in nums):
        #         output.append(i)
        # return output

        num_counts = Counter(nums)
        nums_set = set(nums)  # Convert to set for O(1) membership check
        output = []
        
        for i in nums:
            # Only append if the number occurs once and its neighbors are not in the set
            if num_counts[i] == 1 and (i + 1 not in nums_set) and (i - 1 not in nums_set):
                output.append(i)
        
        return output

                
        
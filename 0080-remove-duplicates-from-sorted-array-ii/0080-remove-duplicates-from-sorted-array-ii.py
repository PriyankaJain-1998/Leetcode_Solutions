from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key, value in count.items():
            if value > 2: 
                num_times_remove = value - 2
                for i in range (num_times_remove):
                    nums.remove(key)
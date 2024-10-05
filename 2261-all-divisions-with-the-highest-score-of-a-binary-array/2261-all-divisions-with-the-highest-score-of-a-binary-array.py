class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # score = {}
        # for i in range(len(nums)+1):
        #     left,right = nums[0:i], nums[i:]
        #     score[i] = left.count(0)+right.count(1)

        # max_value = max(score.values())
        # keys_with_max_value = [key for key, value in score.items() if value == max_value]

        # return keys_with_max_value

        total_zeros = nums.count(0)  # Count total number of 0's
        left_zeros = 0  # Count of 0's in the left part
        right_ones = nums.count(1)  # Initial count of 1's in the right part
        score = {}
        
        # Loop through the nums array to calculate scores efficiently
        for i in range(len(nums) + 1):
            # Calculate score at each split
            score[i] = left_zeros + right_ones
            
            # If we haven't processed all numbers yet
            if i < len(nums):
                if nums[i] == 0:
                    left_zeros += 1  # Increment left's count of 0's
                if nums[i] == 1:
                    right_ones -= 1  # Decrement right's count of 1's
        
        max_value = max(score.values())
        keys_with_max_value = [key for key, value in score.items() if value == max_value]
        
        return keys_with_max_value
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerocount = nums.count(0)
    
        # Remove all zeros from the list
        nums[:] = [i for i in nums if i != 0]  # Modify nums in-place
        
        # Append the correct number of zeros at the end
        nums.extend([0] * zerocount)
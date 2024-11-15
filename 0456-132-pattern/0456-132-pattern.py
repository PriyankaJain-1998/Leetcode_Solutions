class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False  # A 132 pattern is not possible with fewer than 3 elements

        stack = []  # This will store potential 'nums[k]' values
        second_element = float('-inf')  # This will store the 'nums[k]' value we are considering

        # Traverse the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_element:
                return True  # Found a valid 132 pattern
            while stack and nums[i] > stack[-1]:
                second_element = stack.pop()  # Update the 'second_element' as the top of the stack
            stack.append(nums[i])  # Push the current element onto the stack

        return False
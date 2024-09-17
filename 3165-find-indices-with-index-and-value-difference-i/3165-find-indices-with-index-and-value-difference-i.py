class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]
        if indexDifference == valueDifference == 0: return [0,0]
        for i in range(n):
            for j in range(i + 1, n):
                if abs(j - i) >= indexDifference and abs(nums[j] - nums[i]) >= valueDifference:
                    # Update the answer with the current pair if it meets the conditions
                    if ans[0] == -1 or (i < ans[0] or (i == ans[0] and j < ans[1])):
                        ans[0] = i
                        ans[1] = j

        return ans
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map, ans, stack  = {}, [], [nums2[0]]
        for i in range(1,len(nums2)):
            while stack and nums2[i]>stack[-1]: 
                nums2_map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for ele in stack:
            nums2_map[ele]=-1
        for i in nums1:
            ans.append(nums2_map[i])
        return ans
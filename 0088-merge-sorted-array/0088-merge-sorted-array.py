class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        while (i<m+n):
            nums1[i] = nums2[i-m]
            i+=1
        nums1.sort()
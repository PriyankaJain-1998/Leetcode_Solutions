class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1, nums2, ans = nums[:n], nums[n:], []
        for i in range(n):
            ans.append(nums1[i])
            ans.append(nums2[i])

        return ans
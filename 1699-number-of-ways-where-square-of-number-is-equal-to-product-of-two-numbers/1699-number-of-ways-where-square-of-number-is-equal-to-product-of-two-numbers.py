from itertools import combinations
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        # Helper function to count pairs in a list that match a certain product
        def count_pairs(lst, target_product):
            count = 0
            freq = defaultdict(int)
            for num in lst:
                if target_product % num == 0:
                    count += freq[target_product // num]
                freq[num] += 1
            return count

        # Count Type 1 Triplets
        type1_count = 0
        for i in range(n1):
            num1_squared = nums1[i] ** 2
            type1_count += count_pairs(nums2, num1_squared)

        # Count Type 2 Triplets
        type2_count = 0
        for i in range(n2):
            num2_squared = nums2[i] ** 2
            type2_count += count_pairs(nums1, num2_squared)

        return type1_count + type2_count
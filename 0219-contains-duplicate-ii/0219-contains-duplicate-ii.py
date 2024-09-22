class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## tle
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]==nums[j] and abs(i-j)<=k and i!=j: return True

        ## tle - one liner
        # return any(abs(i - j) <= k for i in range(len(nums)) for j in range(len(nums)) if nums[i] == nums[j] and i != j)

        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map and abs(i - num_map[nums[i]]) <= k:
                return True
            num_map[nums[i]] = i  # Update the latest index of the current number

        return False
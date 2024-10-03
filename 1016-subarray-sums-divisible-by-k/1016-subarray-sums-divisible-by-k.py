class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # output = 0
        # for i in range (len(nums)):
        #     curr_sum = 0
        #     for j in range(i,len(nums)):
        #         curr_sum+=nums[j]
        #         if curr_sum%k==0: output+=1
        # return output

        prefix_sum = 0
        remainder_count = {0: 1}
        output = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            if remainder in remainder_count:
                output += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return output
                        
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ## --- CAUSES TLE
        ## -- BRUTE FORCE : O(n*2)
        # ans, even_sum = [], 0
        # for i in queries:
        #     value,index = i[0],i[1]
        #     nums[index]+=value
        #     for j in nums:
        #         if j%2==0:
        #             even_sum +=j
        #     ans.append(even_sum)
        #     even_sum=0
        # return ans

        sum_even = 0
        output = []
        for i in nums:
            if i%2==0: sum_even+=i
        for i in queries:
            value,index = i[0],i[1]
            if nums[index]%2==0: sum_even -= nums[index]
            nums[index]+=value
            if nums[index]%2==0:
                sum_even +=nums[index]
            output.append(sum_even)
         
        return output



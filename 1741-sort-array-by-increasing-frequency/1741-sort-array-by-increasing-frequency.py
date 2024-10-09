class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        # sorted_c = dict(sorted(c.items(), key=lambda item: item[1]))
        # print(c, sorted_c)
        # ans=[]
        # for k,v in sorted_c.items():
        #     a = [k]*v
        #     ans+=a
        # print(ans)
        # return ans

        nums.sort(key=lambda x:(c[x], -x))
        return nums
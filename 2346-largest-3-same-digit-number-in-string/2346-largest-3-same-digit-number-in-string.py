class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # num_set = set(num)
        # max_num = []
        # for i in num_set: 
        #     print(i, num.count(i))
        #     if num.count(i)>=3:
        #         indices_list = [index for index, digit_ in enumerate(num) if digit_ == i]
        #         print(indices_list)
        #         if list(range(min(indices_list), max(indices_list)+1)) == indices_list:
        #             max_num.append(i)
        # if max_num: return str(max(max_num))*3
        # else: return ""
        n = num
        return max(n[i-2:i+1] if n[i] == n[i - 1] == n[i - 2] else "" for i in range(2, len(n)))


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        divisors, output = num, 0
        for i in range (0, len(str(num))-k+1):
            curr_subarray = int(str(num)[i:i+k])
            if curr_subarray>0:
                if divisors % curr_subarray == 0 : output+=1
        return output

        
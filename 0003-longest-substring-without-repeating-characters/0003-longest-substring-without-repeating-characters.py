class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # output = 0
        # window_size = len(s)
        # while (window_size>1):
        #     s_ = s[0:window_size]
        #     print(window_size, s[0:window_size])
        #     if len(set(s_))==1: output = len(s_)
        #     if len(set(s_))==window_size: 
        #         print("*",s[0:window_size], set(s_))
        #         if output<len(set(s_)):
        #             output = len(set(s_))
        #     window_size-=1

        # window_size = 0
        # output_ = 0
        # print("*"*10)
        # while (window_size<len(s)):
        #     s_ = s[window_size:]
        #     print(window_size, s[0:window_size])
        #     if len(set(s_))==1: output_ = len(s_)
        #     if len(set(s_))==window_size: 
        #         print("*",s[0:window_size], set(s_))
        #         if output_<len(set(s_)):
        #             output_ = len(set(s_))
        #     window_size+=1
        # print(output_, output)
        # if output_>output: return output_
        # else:
        #     return output


        if len(s) == 1: return 1
        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
                print(s_result)
            else:
                s_result = s_result[s_result.index(i)+1:] + i
                print("*",s_result)
                
            if len(s_result) > count:
                count = len(s_result)
        
        return count

        
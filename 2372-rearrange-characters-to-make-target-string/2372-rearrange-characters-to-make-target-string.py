class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # set_t = set(target)
        # # return (min(s.count(i) for i in set_t))
        # output = 999999
        # for i in set_t:
        #     if s.count(i)==len(target) and len(set_t)==1: return 1
        #     else: output = min(output, s.count(i))
        # return output


        maxx = []
        for i in range(len(set(target))):
            t_count = target.count(target[i]) # count the no of occurrence of letter in target string
            s_count = s.count(target[i]) # count the no of occurrence of target letter in s
            if t_count <= s_count:
                maxx.append(s_count // t_count)
            else:
                return 0
        return min(maxx)
class Solution:
    def clearDigits(self, s: str) -> str:
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i].isdigit():
        #         del s[i]
        #         del s[i-1]
        #         print(s)
        stack = []  
        for i in s: 
            if i.isdigit():
                stack.pop()
                # index = s.index(i)
                # s = s.replace(i,"").replace(s[index-1],"",1)
                # print(index, s)
            else: stack.append(i)
        print(stack)
        return "".join(stack)
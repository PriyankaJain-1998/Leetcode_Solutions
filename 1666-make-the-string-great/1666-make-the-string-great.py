class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            # if len(stack)>0:
            #     if s[i].isupper():
            #         if stack[-1].lower() == s[i].lower(): stack.pop()
            #     else: stack.append(s[i])  
            if stack and stack[-1].lower() == i.lower() and stack[-1] != i: stack.pop()
            else: 
                stack.append(i)
        return "".join(stack)
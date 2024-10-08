class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # stack = []
        # for i in s:
        #     stack.append(i)
        #     if "".join(stack[-len(part):]) == part: 
        #         for i in range(len(part)): stack.pop()
            
        # return "".join(stack)

        while part in s:
            s = s.replace(part,"", 1)
        return s
        
        


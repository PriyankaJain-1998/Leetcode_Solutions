class Solution:
    def minLength(self, s: str) -> int:
        string = ["AB", "CD"]
        stack = []
        if "AB" or "CD" in s: 
            for i in s: 
                stack.append(i)
                if len(stack)>1:
                    print(stack, stack[-1], stack[-2])
                    if stack[-2]+stack[-1] in string: 
                        stack.pop()
                        stack.pop()
            return len(stack)
        else: return len(s)
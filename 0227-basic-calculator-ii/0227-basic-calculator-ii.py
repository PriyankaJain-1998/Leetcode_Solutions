class Solution:
    def calculate(self, s: str) -> int:
        num, presign, stack=0, "+", []
        for i in s+'+':
            if i.isdigit():
                num = num*10 +int(i)
            elif i in '+-*/':
                if presign =='+':
                    stack.append(num)
                if presign =='-':
                    stack.append(-num)
                if presign =='*':
                    stack.append(stack.pop()*num)
                if presign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                presign = i
                num = 0
        return sum(stack)
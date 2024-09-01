class Solution:
    def decodeString(self, s: str) -> str:
        num,stack, res = 0, [],""
        for i in s:
            if i.isdigit(): num = num*10+int(i)

            elif i == "[":
                stack.append(res)
                stack.append(num)
                res = ""
                num = 0
            elif i=="]":
                pnum = stack.pop()
                pstr = stack.pop()
                res = pstr+pnum*res
            else: res +=i
        return res
        
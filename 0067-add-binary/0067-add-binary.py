class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # diff = abs(len(a)-len(b))
        # carry, output = 0, ''
        # if len(a)>len(b): b = diff*'0'+b
        # else: a = diff*'0'+a

        # for i in range(len(a)-1,-1,-1):
            
        #     if a[i]=='1' and b[i]=='1': 
        #         carry = '1'
        #         output = '0' + output

        #     elif a[i]=='0' and b[i]=='0':
        #         if carry=='1': output = '1' + output
        #         else: output = '0' + output

        #     elif (a[i]=='1' and b[i]=='0') or (a[i]=='0' and b[i]=='1'):
        #         if carry=='1': 
        #             output='0'+ output
        #         else: output='1'+ output

        # if carry=='1': output='1'+ output
        # return output


        result = []
        carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
    
            carry = total // 2
        return ''.join(reversed(result))
        
        
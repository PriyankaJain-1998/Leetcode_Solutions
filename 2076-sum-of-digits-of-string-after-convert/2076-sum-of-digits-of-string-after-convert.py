class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
        'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        string_number_code = ""
        for i in range(len(s)):
            string_number_code+=str(alphabet[s[i]])
        digit_sum = 0
        while(k>0):
            while(string_number_code!='0'):
                digit_sum += int(string_number_code)%10
                string_number_code = str(int(string_number_code)//10)
            k-=1
            if k != 0: 
                string_number_code = str(digit_sum)
                digit_sum = 0
        
        return digit_sum

class Solution:
    def maximumTime(self, time: str) -> str:
        # time = time.split(":")
        # print(time)

        # if "?" in time[0]:
        #     time_0_index = time[0].index("?")
        #     print(time_0_index)
        #     if time_0_index==1: 
        #         if (time[0][0]=='0' or time[0][0]=='1'):
        #             time[0] = time[0][0] + '9'
        #         if (time[0][0]=='2'): 
        #             time[0] = time[0][0] + '3'

        #     elif time_0_index==0:
        #         if time[0][1]=='0': time[0] = '0'+time[0][1]
        #         if (int(time[0][1]) in range(1,4)):
        #             time[0] = '2' + time[0][1]
        #         if (int(time[0][1]) in range(4,10)):
        #             time[0] = '1' + time[0][1]
                
        # if "?" in time[1]:
        #     time_1_index = time[1].index("?")
        #     if time_1_index==0:
        #         # if time[1][1]=='0': time[1]= '00'
        #         if int(time[1][1]) in range(0,10):
        #             time[1] = '5'+time[1][1]
        #     elif time_1_index==1:
        #         if time[1][0]=='0': time[1]= '00'
        #         if int(time[1][0]) in range(1,6):
        #             time[1] = time[1][0]+'9'
        
        # print(time)

        # return ":".join(time)

        s=list(time)
        for i in range(len(s)):
            if s[i]=='?':
                if i==0:
                    if s[i+1] in ['0','1','2','3','?']:
                        s[i]='2'
                    else:
                        s[i]='1'
                elif i==1:
                    if s[i-1]=='1' or s[i-1]=='0':
                        s[i]='9'
                    else:
                        s[i]='3'
                elif i==3:
                    s[i]='5'
                elif i==4:
                    s[i]='9'
        return ''.join(s)

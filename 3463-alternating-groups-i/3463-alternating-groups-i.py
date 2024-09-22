class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        a = ['101', '010']
        colors.append(colors[0])
        colors.append(colors[1])
        window_size, count = 3, 0
        for i in range(len(colors)):
            check = colors[i:i+window_size]
            # if window_size-len(check)==1: check.append(colors[0])
            # elif window_size-len(check)==2: 
            #     check.append(colors[0])
            #     check.append(colors[1])

            if ''.join(map(str,check)) in a:
                count+=1

        return count


        
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        a = ['101', '010']
        colors.append(colors[0])
        colors.append(colors[1])
        window_size, count = 3, 0
        for i in range(len(colors)):
            if ''.join(map(str,colors[i:i+window_size])) in a:
                count+=1

        return count


        
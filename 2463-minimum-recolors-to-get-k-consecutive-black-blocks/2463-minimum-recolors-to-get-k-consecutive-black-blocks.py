class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        output = 99999
        for i in range(len(blocks)):
            sub_str = blocks[i:i+k]
            num_oper = sub_str.count('W')
            print(blocks[i:i+k], blocks[i:i+k].count("W"))
            if len(sub_str)!=k:break
            if num_oper == 0: return 0
            else: output = min(output, num_oper)

        return output
        
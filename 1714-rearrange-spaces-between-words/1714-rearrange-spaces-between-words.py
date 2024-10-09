class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(" ")
        print(total_spaces)
        if total_spaces == 0: return text
        text = text.split()
        if len(text)==1:
            return text[0] + total_spaces*" "
        spaces_can_be_input = total_spaces//(len(text)-1)
        print("original:", spaces_can_be_input)
        ans = ""

        for i in range(len(text)):
                

                if i==len(text)-1:
                    ans+=text[i] + total_spaces*" "
                else:
                    ans+=text[i] + spaces_can_be_input*" "
                    total_spaces -=spaces_can_be_input
        print(ans)
        return ans

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        ans = ""
        if ch not in word: return word
        for w in range(len(word)): 
            if word[w]!=ch: stack.append(word[w])
            else: 
                ans += word[w]
                while len(stack)>0:
                    ans += stack.pop()
                ans += word[w+1:]
                return ans
            # break
        
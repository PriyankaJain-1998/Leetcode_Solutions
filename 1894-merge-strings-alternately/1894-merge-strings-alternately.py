class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans, w = "", ""
        wl1, wl2 = len(word1), len(word2)
        if wl1>wl2: w = word1[wl2:]
        elif wl1<wl2: w = word2[wl1:]
        for i,j in zip(word1,word2):
            ans+=i
            ans+=j
        ans+=w
        return ans
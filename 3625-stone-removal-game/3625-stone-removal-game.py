class Solution:
    def canAliceWin(self, n: int) -> bool:
        # if n<10: return False
        count, pile = 0, 10 
        while n>=pile:
            n-=pile
            pile-=1
            count +=1
        return count%2!=0
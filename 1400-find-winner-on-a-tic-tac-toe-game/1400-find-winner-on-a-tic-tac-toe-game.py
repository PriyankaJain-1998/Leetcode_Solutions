class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A=[0]*8
        B=[0]*8
        for i in range(len(moves)):
            r,c=moves[i]
            player = A if i%2==0 else B
            player[r] += 1
            player[c+3] += 1
            if r==c:
                player[6] += 1
            if r==2-c:
                player[7] += 1
        for i in range(8):
            if A[i]==3:
                return "A"
            if B[i]==3:
                return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"
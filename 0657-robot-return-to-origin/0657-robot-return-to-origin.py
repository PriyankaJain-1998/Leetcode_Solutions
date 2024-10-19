class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # directions = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[0,-1]}
        # moves = list(moves)
        # position = [0,0]
        # for move in moves:
        #     position = list(map(lambda x,y:x+y, position, directions[move]))
        #     print(position)
        # if position ==[0,0]: return True
        # else: return False

        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
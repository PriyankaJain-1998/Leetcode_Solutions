class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score, reverse=True)
        
        if len(score)==1: score[score.index(score_sorted[0])] = 'Gold Medal'
        elif len(score)==2: 
            score[score.index(score_sorted[0])] = 'Gold Medal'
            score[score.index(score_sorted[1])] = 'Silver Medal'
        else:
            score[score.index(score_sorted[0])] = 'Gold Medal'
            score[score.index(score_sorted[1])] = 'Silver Medal'
            score[score.index(score_sorted[2])] = 'Bronze Medal'

        for i in range(3, len(score_sorted)):
            score[score.index(score_sorted[i])] = str(i+1)

        return score
            


        
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first, last = rounds[0], rounds[-1]
        if last>=first: return [i for i in range(first,last+1)]
        else:
            rec = []
            for i in range(n):
                if i+1<=last or i+1>=first: rec.append(i+1)
            return sorted(rec)
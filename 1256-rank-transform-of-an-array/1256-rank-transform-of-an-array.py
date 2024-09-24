class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # if len(set(arr))==1: return [1]*len(arr)
        sorted_arr = sorted(set(arr))
        rank = {}
        for i, ele in enumerate(sorted_arr):
            rank[ele] = i+1
        return list(map(rank.get, arr))
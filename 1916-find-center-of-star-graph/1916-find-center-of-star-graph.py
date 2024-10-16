class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center = set(edges[0])
        for i in range(1,len(edges)):
            center = center&set(edges[i])
        return list(center)[0]
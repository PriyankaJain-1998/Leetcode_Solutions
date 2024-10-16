class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # center = set(edges[0])
        # for i in range(1,len(edges)):
        #     center = center&set(edges[i])
        # return list(center)[0]

        if edges[1][0] == edges[0][0] or edges[1][0] == edges[0][1]:
            return edges[1][0]
        return edges[1][1]  
         
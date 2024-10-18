class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = {}
        for i, pt in enumerate(points):
            p1, p2 = pt 
            distance[(p1,p2,i)] = (p1**2 + p2**2)**0.5

        distance = sorted(distance.items(), key=lambda item: item[1])
        distance = distance[:k]
        final = []
        for i in distance:
            final.append(list(i[0])[:2])
        return final
        
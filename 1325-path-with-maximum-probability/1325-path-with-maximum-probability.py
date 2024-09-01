class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g, dq = defaultdict(list), deque([start_node])
        for i,(a,b) in enumerate(edges):
            g[a].append([b,i])
            g[b].append([a,i])
        p = [0.0]*n
        p[start_node]=1.0
        while dq:
            curr = dq.popleft()
            for neighbor, i in g[curr]:
                if p[curr]*succProb[i] > p[neighbor]:
                    p[neighbor] = p[curr] * succProb[i]
                    dq.append(neighbor)
        return p[end_node]

                
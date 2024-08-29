# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         for i in stones:
#             r, c = i[0], i[1]
#             if [r-1, c] in stones: 
#                 del stones[stones.index([r-1,c])]
#                 print(stones)
#             if [r+1, c] in stones: 
#                 del stones[stones.index([r+1,c])]
#                 print(stones)
#             if [r, c-1] in stones: 
#                 del stones[stones.index([r,c-1])]
#                 print(stones)
#             if [r, c+1] in stones: 
#                 del stones[stones.index([r,c+1])]
#                 print(stones)
#         return len(stones)

class Solution:
    def dfs(self, node, adj, visited):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                self.dfs(neighbor, adj, visited)
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]
        
        # Build the graph
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = set()
        numComponents = 0

        # Find the number of connected components
        for i in range(n):
            if i not in visited:
                self.dfs(i, adj, visited)
                numComponents += 1

        return n - numComponents
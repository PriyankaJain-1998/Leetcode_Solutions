class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         grid_ = sum(grid, [])
#         col_data = []
#         for i in range (n):
#             grid[i] = "".join(str(x) for x in grid[i])
#         print(grid)

#         for k in range(n):
#             col_data.append("".join(str(x) for x in grid_[k:len(grid_):n]))
#         print(col_data)
#         # for j, ele in enumerate([grid_[0:len(grid_):n], grid_[1:len(grid_):n], grid_[2:len(grid_):n]]):
#         #     temp.append("".join(str(x) for x in ele))
#         # print(temp)
#         count = 0
#         if grid == col_data: return len(col_data)
#         for i in grid:
#             if i in col_data: 
#                 count+=col_data.count(i)
#                 # temp.remove(i)
#         return count
        tpse = Counter(zip(*grid))                
        grid = Counter(map(tuple,grid))            

        return  sum(tpse[t]*grid[t] for t in tpse)  # <-- compute the number of identical pairs
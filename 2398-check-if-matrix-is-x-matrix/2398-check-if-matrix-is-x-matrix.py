class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n =len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((i==j) or ((i+j)==(n-1))): 
                    print((grid[i][j]))
                    if grid[i][j] == 0: return False
                elif grid[i][j] != 0: return False
                
        return True
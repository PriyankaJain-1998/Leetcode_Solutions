class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_data = [0]*m
        col_data = [0]*n
        
        for tup in indices:
            row_data[tup[0]] = row_data[tup[0]] + 1
            col_data[tup[1]] = col_data[tup[1]] + 1
        
        odd_count = 0 
        for rowp in range(m):
            for colp in range(n):
                val = row_data[rowp] + col_data[colp]
                if val % 2 != 0:
                    odd_count+=1
        
        return odd_count
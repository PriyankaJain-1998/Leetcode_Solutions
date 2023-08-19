#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
from operator import add
from functools import reduce

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # matrix_1d = reduce(add ,matrix)
        # len_matrix = len(matrix)## total number of rows
        # sequence = matrix_1d[0:len(matrix[0])]
        
        # if (len_matrix == 1):
        #     return sequence
        # else:
        #     # del(matrix_1d[0:4])
        #     print(len_matrix)
        #     index_indicator = 0
        #     for i in range(1,len_matrix):
                
        #         # if (i == len_matrix-2):
        #         index_indicator = i*len(matrix[0])+len(matrix[0])-1
                
        #         print(i*len(matrix[0])+len(matrix[0])-1," ",matrix_1d[i*len(matrix[0])+len(matrix[0])-1])
                
        #         sequence.append(matrix_1d[i*len(matrix[0])+len(matrix[0])-1])

        #     print(sequence)
        #     if set(matrix_1d) == set(sequence):
        #         return sequence
        #     else:
        #         # sequence.append(matrix_1d[len(matrix_1d)-len_matrix:])
        #         for i in range(len(matrix_1d)-2, index_indicator,-1 ):
        #             sequence.append(matrix_1d[i])
        #         # sequence.append(matrix_1d[index_indicator+1: len(matrix_1d)-1])

                
        #         for i in range(len(matrix[0]),index_indicator):
        #             sequence.append(matrix_1d[i])
                

        #         return sequence

        ans = []
        for i in matrix:
            if (len(matrix) == 0):
                return ans
        
            m = len(matrix)
            n = len(matrix[0])
            seen = [[0 for i in range(n)] for j in range(m)]
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
            x = 0
            y = 0
            di = 0
        
            # Iterate from 0 to R * C - 1
            for i in range(m * n):
                ans.append(matrix[x][y])
                seen[x][y] = True
                cr = x + dr[di]
                cc = y + dc[di]
        
                if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
                    x = cr
                    y = cc
                else:
                    di = (di + 1) % 4
                    x += dr[di]
                    y += dc[di]
            return ans
                
# @lc code=end


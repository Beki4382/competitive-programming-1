class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        locations= []
        r, c= 0, 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    locations.append((i, j))
        for x,y in locations:
            
            for i in range(len(matrix)):
                matrix[i][y]=0
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
        
            
            
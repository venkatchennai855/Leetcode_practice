class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col=1

        for i in range(0,n):
            for j in range(0,m): 
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    if(j!=0):
                        matrix[0][j]=0
                    else:
                        col=0
        for i in range(1,n):
            for j in range(1,m): 
                if(matrix[i][j]!=0):
                    if(matrix[i][0]==0 or matrix[0][j]==0):
                        matrix[i][j]=0

        if(matrix[0][0]==0):
            for j in range(m):
                matrix[0][j]=0
        if(col==0):
            for i in range(n) :
                matrix[i][0]=0          
        
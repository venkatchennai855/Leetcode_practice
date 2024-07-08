class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        exist= False
        flag=-1
        for i in range(n):
            if(target<=matrix[i][m-1]):
                flag=i
                break
        for i in range(m):
            if(matrix[flag][i]==target):
                exist=True
                break
        
        return exist
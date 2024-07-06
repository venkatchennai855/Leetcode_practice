class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def comb(n,r):
            res=1
            for i in range(r):
                res=res*(n-i)
                res=res//(i+1)
            return res
        n=numRows
        ans=[]
        for i in range(n):
            l=[]
            for j in range(i+1):
                x=comb(i,j)
                l.append(x)
            ans.append(l)   

        return ans
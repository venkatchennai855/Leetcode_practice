class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)-1
        m=len(s)-1
        cnt=0
        while(n>=0 and m>=0):
            if(g[n]<=s[m]):
                cnt+=1
                n-=1
                m-=1
            else:
                n-=1
        return cnt



def ed(n,m,s1,s2,dp):
    if n==0:
        return m
    if m==0:
        return n
    if dp[n][m]!= 0:
        return dp[n][m]
    if (s1[n-1]==s2[m-1]):
        dp[n][m]= 0+ ed(n-1,m-1,s1,s2,dp)
        return dp[n][m]
    dp[n][m]= 1+min(ed(n-1,m-1,s1,s2,dp),min(ed(n,m-1,s1,s2,dp),ed(n-1,m,s1,s2,dp)))
    return dp[n][m]
class Solution:
	def editDistance(self, str1, str3):
	    n = len(str1)
        m = len(str3)
	    dp=[[0 for i in range(m+1)] for j in range(n+1)]
		return ed(n,m,str1,str3,dp)

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends
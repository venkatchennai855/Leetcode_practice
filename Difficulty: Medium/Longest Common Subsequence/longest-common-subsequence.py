#User function Template for python3
cnt=0
# def dummy(n,m,s1,s2,dp):
#     if(n==0 or  m==0):
#         return 0
#     if(dp[n][m]!=-1):
#         return dp[n][m]
#     if(s1[n-1]==s2[m-1]):
        
#         dp[n][m]=1+dummy(n-1,m-1,s1,s2,dp)
#         return dp[n][m]
#     dp[n][m]= max(dummy(n-1,m,s1,s2,dp),dummy(n,m-1,s1,s2,dp))
#     return dp[n][m]
def dummy(n,m,s1,s2):
    
    dp=[[0 for i in range(m+1)]for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[n][m]
        
class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        #dp=[[-1 for i in range(m+1)]for j in range(n+1)]
        return dummy(n,m,str1,str2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        str1 = str(input())
        str2 = str(input())
        ob = Solution()
        print(ob.lcs(n, m, str1, str2))

# } Driver Code Ends
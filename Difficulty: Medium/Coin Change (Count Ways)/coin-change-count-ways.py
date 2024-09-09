# #User function Template for python3
# def allways(coins,N,Sum,dp):
#     if(Sum==0):
#         dp[N][Sum]=1
#         return dp[N][Sum]
#     if(Sum <= 0 or N==0):
#         return 0
#     if(dp[N][Sum]!=-1):
#         return dp[N][Sum]
        
#     dp[N][Sum]=allways(coins,N,Sum-coins[N-1],dp)+allways(coins,N-1,Sum,dp)
#     return dp[N][Sum]
    
    
def tab(coins,N,Sum):
    dp=[[0 for j in range(Sum+1)]for j in range(N+1)]

    for i in range(N+1):
        dp[i][0]=1
    
    for i in range(1,N+1):
        for j in range(1,Sum+1):
            dp[i][j]=dp[i-1][j]
            if(j-coins[i-1]>=0):
                dp[i][j]+=dp[i][j-coins[i-1]]
            
    return dp[N][Sum]
class Solution:
    def count(self, coins, N, Sum):
        # dp=[[-1 for j in range(Sum+1)]for j in range(N+1)]
        return tab(coins,N,Sum)
         



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends
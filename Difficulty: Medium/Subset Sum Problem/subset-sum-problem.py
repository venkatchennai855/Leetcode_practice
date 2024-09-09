#User function Template for python3
def subsum(N,arr,Sum,dp):
    if(Sum==0):
        dp[N][Sum]=True
        return dp[N][Sum]
    if(N==0):
        dp[N][Sum]=False
        return dp[N][Sum]
    if(dp[N][Sum] is not None):
        return dp[N][Sum]
    if(arr[N-1]>Sum):
        dp[N][Sum]= subsum(N-1,arr,Sum,dp)
        return dp[N][Sum]
    dp[N][Sum]=subsum(N-1,arr,Sum,dp) or subsum(N-1,arr,Sum-arr[N-1],dp)
    return dp[N][Sum]
class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp=[[None for i in range(sum+1)] for j in range(N+1) ]
        return subsum(N,arr,sum,dp)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
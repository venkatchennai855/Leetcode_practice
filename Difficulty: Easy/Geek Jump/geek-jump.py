#User function Template for python3
import sys
class Solution:
    def solve(self,dp,height, n):
        if n==0:
            return 0
        R2=sys.maxsize
        if (dp[n]!=-1):
            return dp[n]
            
        R1=self.solve(dp,height,n-1)+abs(height[n]-height[n-1])
        
        if n>1:
            R2=self.solve(dp,height,n-2)+abs(height[n]-height[n-2])
        dp[n]=min(R1,R2)
        return dp[n]
    def minimumEnergy(self, height, n):
        dp=[-1 for i in range(n)]
        return self.solve(dp,height,n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
        print("~")
# } Driver Code Ends
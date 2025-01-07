class Solution:
    def solvedp(self,n,dp):
        if n==1:
            return 1
        if n==0:
            return 1
        if dp[n]!=0:
            return dp[n]
        dp[n]=self.solvedp(n-1,dp)+self.solvedp(n-2,dp)
        return dp[n]

        return self.solvedp(n-1,dp)+self.solvedp(n-2,dp)
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        x = self.solvedp(n,dp)
        return x
def steps(n,dp):
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(dp[n]!=0):
        return dp[n]
    dp[n]=steps(n-1,dp)+steps(n-2,dp)
    return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        return steps(n,dp)
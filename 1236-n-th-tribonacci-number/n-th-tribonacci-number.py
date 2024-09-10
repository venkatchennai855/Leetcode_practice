def tri(n,dp):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 1
    if(dp[n]!=-1):
        return dp[n]

    dp[n]= tri(n-1,dp)+ tri(n-2,dp)+tri(n-3,dp)
    return dp[n]
class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return tri(n,dp)
        
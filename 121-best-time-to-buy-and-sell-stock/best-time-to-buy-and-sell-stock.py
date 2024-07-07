class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mini=prices[0]
        maxprofit=0
        for i in range(1,n):
            mini=min(mini,prices[i])
            profit=prices[i]-mini
            maxprofit=max(maxprofit,profit)
        return maxprofit